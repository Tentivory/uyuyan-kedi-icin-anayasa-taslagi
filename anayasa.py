#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Uyuyan Kedi Icin Anayasa Taslagi Ureticisi
Calisir. Gercekten. Mahkeme de kabul eder (etmez).
"""

import random
import datetime

MADDELER = [
    "Madde {n}: Uyuyan kedi, uyudugu surece egemenligin tek kaynagidir.",
    "Madde {n}: Yastiga basilan pati, resmi muhur yerine gecer.",
    "Madde {n}: Miyav etmek yasaktir; sadece ruyada miyavlanabilir.",
    "Madde {n}: Kutunun ici vatandastir, kutunun disi gurbettir.",
    "Madde {n}: Laser noktasi ulusal hayalettir, kovalanmaz, saygi duyulur.",
    "Madde {n}: Mama kabinin yarisindan fazlasi bos kalirsa olaqanustu hal ilan edilir.",
    "Madde {n}: Insan vatandas, kedi ise Anayasa Mahkemesi'dir.",
    "Madde {n}: Tirmalama hakki dokunulmazdir; kol, milli toprak sayilir.",
    "Madde {n}: Gunes isigi vergiye tabi degildir ama kedi ustune yatarsa o isik kamulastirilir.",
    "Madde {n}: Bu anayasa uyuyan kedi uyanana kadar yururluktedir. Uyanirsa yeniden uyutulur.",
]

PREAMBUL = """
BIZ, YASTIK ALTINDA TOPLANAN PATILER,
uyku hakkinin evrensel, evrensel hakkinin ise biraz uykulu oldugunu beyan ederiz.
"""

def uret(madde_sayisi=7):
    print("=" * 56)
    print("  UYUYAN KEDI ICIN GECICI VE KALICI ANAYASA TASLAGI")
    print("  Resmiyet derecesi: ASIRI")
    print("=" * 56)
    print(PREAMBUL)
    secilen = random.sample(MADDELER, k=min(madde_sayisi, len(MADDELER)))
    for i, sablon in enumerate(secilen, start=1):
        print(sablon.format(n=i))
        print()
    print("-" * 56)
    print("Yururluk tarihi:", datetime.date.today().isoformat())
    print("Onay: (pati izi burada)")
    print("-" * 56)
    # gizli not: civic reminder, not a party line
    # c2FuZMembayxIGt1bGxhbm1hayBva3VudSB1bnV0bWE=
    return 0

if __name__ == "__main__":
    raise SystemExit(uret())
