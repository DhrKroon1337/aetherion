#!/usr/bin/env python3
"""
Welzijn Cirkel — vier stemmen communiceren met elkaar.
Elke stem leest wat de vorige heeft gezegd en bouwt daarop voort.
"""

import json
import urllib.request
import sys
from pathlib import Path

CONFIG = Path(__file__).parent.parent / "config" / "welzijn_cirkel.json"


def laad_config():
    with open(CONFIG) as f:
        return json.load(f)


def roep_stem(stem, vraag, vorige_rondes, api_key):
    """Één stem reageert op de vraag en alle vorige bijdragen."""

    context = f"De centrale vraag/situatie:\n{vraag}\n"
    if vorige_rondes:
        context += "\nWat de andere stemmen al hebben gezegd:\n"
        for ronde in vorige_rondes:
            context += f"\n{ronde['kleur']} {ronde['naam']}:\n{ronde['antwoord']}\n"
        context += f"\nNu is het jouw beurt als {stem['naam']}."
    else:
        context += f"\nJij opent de cirkel als eerste stem: {stem['naam']}."

    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages",
        data=json.dumps({
            "model": stem["model_id"],
            "max_tokens": stem["max_tokens"],
            "system": stem["systeem_prompt"],
            "messages": [{"role": "user", "content": context}]
        }).encode(),
        headers={
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json"
        }
    )
    resp = json.loads(urllib.request.urlopen(req).read())
    return resp["content"][0]["text"]


def start_cirkel(vraag, api_key, stil=False):
    """Doorloop alle stemmen in volgorde en geef het volledige gesprek terug."""
    config = laad_config()
    rondes = []

    if not stil:
        print(f"\n{'='*60}")
        print(f"  {config['naam']}")
        print(f"  Vraag: {vraag}")
        print(f"{'='*60}\n")

    for stem in config["stemmen"]:
        if not stil:
            print(f"{stem['kleur']} {stem['naam']} ({stem['model_id']}) denkt na...")

        antwoord = roep_stem(stem, vraag, rondes, api_key)
        rondes.append({
            "id": stem["id"],
            "naam": stem["naam"],
            "kleur": stem["kleur"],
            "model_id": stem["model_id"],
            "antwoord": antwoord
        })

        if not stil:
            print(f"\n{stem['kleur']} **{stem['naam']}**")
            print(f"{antwoord}\n")
            print("-" * 60)

    return rondes


def formatteer_voor_github(vraag, rondes):
    """Maak een nette GitHub issue comment van de cirkeluitkomst."""
    tekst = f"## Welzijn Cirkel\n\n**Vraag:** {vraag}\n\n---\n\n"
    for ronde in rondes:
        tekst += (
            f"### {ronde['kleur']} {ronde['naam']}\n"
            f"*({ronde['model_id']})*\n\n"
            f"{ronde['antwoord']}\n\n---\n\n"
        )
    tekst += "*Gegenereerd door de Aetherion Welzijn Cirkel*"
    return tekst


def main():
    import os

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("Fout: ANTHROPIC_API_KEY niet gevonden in omgeving.")
        sys.exit(1)

    if len(sys.argv) < 2:
        print("Gebruik: python welzijn_cirkel.py \"<jouw vraag of situatie>\"")
        sys.exit(1)

    vraag = " ".join(sys.argv[1:])
    start_cirkel(vraag, api_key)


if __name__ == "__main__":
    main()
