"""
9Router AI Asset Generator for AG-Stick v2.

Generates modular environments, macro prop closeups, and hero frames using
9router cx/gpt-5.5-image. Adheres strictly to the 10-20-70 rule:
- 70% Reusable Vector Rigs (StickmanRig, CameraRig)
- 20% Simple Environments (BG_OMEGA_LAB via 9Router)
- 10% Hero Frames (HERO_BLUE_FLASH via 9Router)
"""

import os
import sys
import json
import base64
import time
import shutil
import urllib.request
from typing import Dict, Any, Optional

URL = "http://127.0.0.1:20128/v1/images/generations"
API_KEY = "sk-c4f2444795b190b3-kzvd4h-ea839762"
MODEL = "cx/gpt-5.5-image"

ROOT_DIR = r"c:\Users\bati-\Documents\AG-Stick"
LOCAL_ASSET_DIR = os.path.join(ROOT_DIR, "projects", "demon-core-10min", "assets", "v2")
REMOTION_PUBLIC_DIR = os.path.join(
    ROOT_DIR, "projects", "wework-47-billion-illusion", "remotion", "public", "assets", "demon_core", "v2"
)

os.makedirs(LOCAL_ASSET_DIR, exist_ok=True)
os.makedirs(REMOTION_PUBLIC_DIR, exist_ok=True)


class AssetGenerator9Router:
    def __init__(self, api_key: str = API_KEY, model: str = MODEL):
        self.api_key = api_key
        self.model = model

    def generate_asset(self, asset_id: str, prompt: str, size: str = "1672x941", force: bool = False) -> str:
        """
        Generates an image asset via 9router cx/gpt-5.5-image.
        Returns local filepath of generated PNG.
        """
        out_file = os.path.join(LOCAL_ASSET_DIR, f"{asset_id}.png")
        remotion_file = os.path.join(REMOTION_PUBLIC_DIR, f"{asset_id}.png")

        if os.path.exists(out_file) and os.path.getsize(out_file) > 10000 and not force:
            print(f"[CACHE] Asset '{asset_id}' already exists ({os.path.getsize(out_file)} bytes).", flush=True)
            if not os.path.exists(remotion_file):
                shutil.copyfile(out_file, remotion_file)
            return out_file

        payload = {
            "model": self.model,
            "prompt": prompt,
            "size": size
        }

        print(f"[9ROUTER] Generating asset '{asset_id}' with {self.model}...", flush=True)
        req = urllib.request.Request(
            URL,
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_key}"
            }
        )

        try:
            t0 = time.time()
            with urllib.request.urlopen(req, timeout=120) as resp:
                res = json.loads(resp.read().decode("utf-8"))
                if "data" in res and len(res["data"]) > 0:
                    item = res["data"][0]
                    img_bytes = None
                    if "b64_json" in item and item["b64_json"]:
                        img_bytes = base64.b64decode(item["b64_json"])
                    elif "url" in item and item["url"]:
                        with urllib.request.urlopen(item["url"], timeout=60) as uresp:
                            img_bytes = uresp.read()

                    if img_bytes:
                        with open(out_file, "wb") as f:
                            f.write(img_bytes)
                        shutil.copyfile(out_file, remotion_file)
                        elapsed = time.time() - t0
                        print(f"[SUCCESS] Asset '{asset_id}' generated in {elapsed:.1f}s ({len(img_bytes)} bytes)!", flush=True)
                        return out_file
                    else:
                        raise RuntimeError("No image data returned from 9router")
                else:
                    raise RuntimeError(f"Unexpected response structure: {res}")
        except Exception as e:
            print(f"[ERROR] Failed to generate '{asset_id}': {e}", flush=True)
            raise


def generate_scene24_modular_assets():
    """Batch generates the modular assets required for Scene 24 in AG-Stick v2."""
    gen = AssetGenerator9Router()

    # 1. Environment: Empty Los Alamos Omega Site Laboratory Workbench Room
    bg_prompt = (
        "Minimalist 2D vector cartoon background of the 1945 Los Alamos Omega Site nuclear laboratory assembly room, "
        "heavy wooden timber workbench in center, analog oscilloscope instruments, copper wire spools, and vintage tools in background, "
        "wooden barrack wall with high window showing twilight desert canyon cliff, dark slate charcoal atmosphere (#12141A, #161822), "
        "subtle amber warning lamp glow (#FFAA00), clean flat vector art, bold outlines, strictly no people, no characters, strictly no text, no letters, no 3D CGI."
    )
    gen.generate_asset("bg_omega_lab", bg_prompt)

    # 2. Macro Closeup: Screwdriver tip wedged in beryllium dome lip (Beat 24c)
    macro_prompt = (
        "Extreme macro closeup 2D vector illustration of two smooth silver-gray beryllium hemispherical dome rims separated by a razor-thin 1-millimeter gap, "
        "the flat steel blade of a yellow-acetate handled flathead screwdriver wedged between the metal lips, metallic reflections and electric cyan rim highlights (#00E5FF), "
        "dark charcoal slate background (#111319), clean 2D vector cartoon, bold 10px black ink outlines, high contrast, strictly no text, no labels, no watermark, no 3D CGI."
    )
    gen.generate_asset("macro_screwdriver_gap", macro_prompt)

    # 3. Hero Climax Frame: Blinding Cherenkov Blue Burst (Beat 24h)
    hero_prompt = (
        "Blinding super-critical Cherenkov radiation blue explosion blooming across a 1940s nuclear laboratory workbench, "
        "intense electric cyan (#00E5FF) and vibrant cobalt radiation flare radiating powerful dynamic vector light beams, "
        "metallic beryllium dome at ground zero, dramatic high-contrast vector shockwave, dark slate room edges (#12141A), "
        "flat 2D vector cartoon art, bold clean ink strokes, strictly no text, no comic speech bubbles, no watermark, no 3D render."
    )
    gen.generate_asset("hero_cherenkov_flash", hero_prompt)


if __name__ == "__main__":
    generate_scene24_modular_assets()
