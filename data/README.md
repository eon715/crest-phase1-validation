# Source Data

This folder documents the public benchmark data sources intended for CREST Phase 1 reproduction.

## Primary Data Targets

CREST Phase 1 uses galaxy-rotation and baryonic mass-model data associated with the SPARC/RAR benchmark family.

Expected source files:

- `SPARC_Lelli2016c.mrt.txt`
- `MassModels_Lelli2016c.mrt.txt`
- `RAR.mrt.txt`
- `BTFR_Lelli2019.mrt.txt`

## Current Repository Status

The present repository does not yet commit the full raw public benchmark datasets directly.

Instead, it includes regenerated Phase 1 summary tables and figures in:

- `assets/phase1_rmse_table.csv`
- `assets/phase1_halo_reference_table.csv`
- `assets/phase1_overlap_cases.csv`

## Reproducibility Plan

Future reproduction scripts should either:

1. Download the public SPARC/RAR files from their original public sources, or
2. Read locally supplied copies of the expected files from this `data/` folder.

The repository should avoid redistributing third-party datasets unless their license clearly allows it.
