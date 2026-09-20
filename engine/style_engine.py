"""
Style Engine for AG-Stick v2.

Loads style.yaml, characters.yaml, and props.yaml.
Provides helpers for character lookup, prop resolution, and tier budget enforcement.
"""

import os
from typing import Dict, Any, Optional
import yaml
from engine.schema import AssetTier


class StyleEngine:
    def __init__(self, style_name: str = "neon-atom", styles_root: Optional[str] = None):
        if styles_root is None:
            # Default to styles/ directory relative to workspace root
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            styles_root = os.path.join(base_dir, "styles")
        
        self.style_dir = os.path.join(styles_root, style_name)
        if not os.path.exists(self.style_dir):
            raise FileNotFoundError(f"Style directory not found: {self.style_dir}")
        
        self.style_config = self._load_yaml("style.yaml")
        self.characters = self._load_yaml("characters.yaml").get("characters", {})
        self.props = self._load_yaml("props.yaml").get("props", {})

    def _load_yaml(self, filename: str) -> Dict[str, Any]:
        path = os.path.join(self.style_dir, filename)
        if not os.path.exists(path):
            return {}
        with open(path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f) or {}

    def get_character(self, char_id: str) -> Optional[Dict[str, Any]]:
        return self.characters.get(char_id)

    def get_prop(self, prop_id: str) -> Optional[Dict[str, Any]]:
        return self.props.get(prop_id)

    def validate_pose(self, char_id: str, pose: str) -> bool:
        char = self.get_character(char_id)
        if not char:
            return False
        return pose in char.get("poses", [])

    def validate_expression(self, char_id: str, expr: str) -> bool:
        char = self.get_character(char_id)
        if not char:
            return False
        return expr in char.get("expressions", [])

    def get_tier_budget_targets(self) -> Dict[str, float]:
        return self.style_config.get("tier_budget_targets", {
            "T0_procedural": 0.35,
            "T1_reusable_asset": 0.30,
            "T2_composed_asset": 0.20,
            "T3_ai_generated": 0.10,
            "T4_hero_cinematic": 0.05
        })

    def get_color(self, color_name: str) -> str:
        palette = self.style_config.get("palette", {})
        return palette.get(color_name, "#FFFFFF")
