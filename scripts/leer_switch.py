#!/usr/bin/env python3
"""Schakel tussen leerprofielen in leerproces.json."""

import json
import sys
from pathlib import Path

CONFIG = Path(__file__).parent.parent / "config" / "leerproces.json"


def laad_config():
    with open(CONFIG) as f:
        return json.load(f)


def sla_op(config):
    with open(CONFIG, "w") as f:
        json.dump(config, f, indent=2, ensure_ascii=False)


def toon_status(config):
    actief = config["actief_profiel"]
    profiel = config["leerprofielen"][actief]
    voortgang = config["voortgang"]
    print(f"\n== Aetherion Leerstatus ==")
    print(f"Actief profiel : {actief} (niveau {profiel['niveau']})")
    print(f"Model          : {profiel['model_id']}")
    print(f"Beschrijving   : {profiel['beschrijving']}")
    print(f"Punten         : {voortgang['punten']}")
    print(f"Lessen gedaan  : {len(voortgang['voltooide_lessen'])}")
    print()


def schakel(profiel_naam):
    config = laad_config()
    if profiel_naam not in config["leerprofielen"]:
        beschikbaar = list(config["leerprofielen"].keys())
        print(f"Onbekend profiel '{profiel_naam}'. Kies uit: {beschikbaar}")
        sys.exit(1)
    config["actief_profiel"] = profiel_naam
    config["voortgang"]["huidig_niveau"] = config["leerprofielen"][profiel_naam]["niveau"]
    sla_op(config)
    print(f"Geschakeld naar profiel: {profiel_naam}")
    toon_status(config)


def voeg_les_toe(les_naam):
    config = laad_config()
    if les_naam not in config["voortgang"]["voltooide_lessen"]:
        config["voortgang"]["voltooide_lessen"].append(les_naam)
        config["voortgang"]["punten"] += 10
        sla_op(config)
        print(f"Les '{les_naam}' voltooid (+10 punten)")
    else:
        print(f"Les '{les_naam}' was al voltooid")
    toon_status(config)


def main():
    if len(sys.argv) < 2:
        toon_status(laad_config())
        print("Gebruik: python leer_switch.py <profiel|status|les <naam>>")
        print("  Profielen: basis | gemiddeld | expert")
        return

    commando = sys.argv[1]
    if commando == "status":
        toon_status(laad_config())
    elif commando == "les" and len(sys.argv) >= 3:
        voeg_les_toe(sys.argv[2])
    elif commando in ("basis", "gemiddeld", "expert"):
        schakel(commando)
    else:
        print(f"Onbekend commando: {commando}")
        sys.exit(1)


if __name__ == "__main__":
    main()
