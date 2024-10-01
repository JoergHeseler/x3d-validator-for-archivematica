# x3d_validator_for_archivematica

**x3d_validator_for_archivematica** is a script that enables [Archivematica](https://www.archivematica.org/) to validate Extensible 3D (X3D) files.

## Installation

To install the **x3d_validator_for_archivematica** script, follow these steps:

### 1. Download the official X3D schemas 

- Create a folder `/usr/share/schemes` and a subfolder `/usr/share/schemes/x3d`.
- Download the [X3D validation package](https://www.web3d.org/specifications/x3d.all.validation.zip) from the official website.
- Unzip this package so that all XSD files are in the `/usr/share/schemes/x3d/` root folder, e. g. `/usr/share/schemes/x3d/x3d-3.3.xsd`.

### 2. Create a new validation command
- In the Archivematica frontend, navigate to **Preservation planning** > **Validation** > **Commands** > **Create new command** or go directly to [this link](http://10.10.10.20/fpr/fpcommand/create/).
- Fill in the following fields:
    - **The related tool**: Select **Archivematica script**.
    - **Description**: Enter `Validate using x3d_validator`.
    - **Script**: Paste the entire content of the **x3d_validator.py** file.
    - **Script type**: Select **Python script**.
    - **Command usage**: Select **Validation**.
- Click **Save**.

### 3. Create a new validation rule for X3D 3.0
- In the Archivematica frontend, navigate to **Preservation planning** > **Validation** > **Rules** > **Create new rule** or go directly to [this link](http://10.10.10.20/fpr/fprule/create/).
- Fill in the following fields:
    - **Purpose**: Select **Validation**.
    - **The related format**: Select **Text (Markup): X3D: X3D v3.0 (fmt/579)**.
    - **Command**: Select **Validate using x3d_validator**.
- Click **Save**.

### 4. Create a new validation rule for X3D 3.1
- In the Archivematica frontend, navigate to **Preservation planning** > **Validation** > **Rules** > **Create new rule** or go directly to [this link](http://10.10.10.20/fpr/fprule/create/).
- Fill in the following fields:
    - **Purpose**: Select **Validation**.
    - **The related format**: Select **Text (Markup): X3D: X3D v3.1 (fmt/580)**.
    - **Command**: Select **Validate using x3d_validator**.
- Click **Save**.

### 5. Create a new validation rule for X3D 3.2
- In the Archivematica frontend, navigate to **Preservation planning** > **Validation** > **Rules** > **Create new rule** or go directly to [this link](http://10.10.10.20/fpr/fprule/create/).
- Fill in the following fields:
    - **Purpose**: Select **Validation**.
    - **The related format**: Select **Text (Markup): X3D: X3D v3.2 (fmt/581)**.
    - **Command**: Select **Validate using x3d_validator**.
- Click **Save**.

### 6. Create a new validation rule for X3D 3.3
- In the Archivematica frontend, navigate to **Preservation planning** > **Validation** > **Rules** > **Create new rule** or go directly to [this link](http://10.10.10.20/fpr/fprule/create/).
- Fill in the following fields:
    - **Purpose**: Select **Validation**.
    - **The related format**: Select **Text (Markup): X3D: X3D v3.3 (fmt/582)**.
    - **Command**: Select **Validate using x3d_validator**.
- Click **Save**.

## Test

To test this validator, you can use the sample X3D files located in the [`test`](./test/) folder.

You can view the error codes and detailed validation results in the Archivmatica frontend after starting a transfer by expanding the `▸ Microservice: Validation` section and clicking on the gear icon of `Job: Validate formats`.

Files with no errors end with the filename `_valid` and should pass validation with this script (i. e. return error code **0**). However, all other files contain errors and should fail validation (i. e. return error code **1**).

## Dependencies

[Archivematica 1.13.2](https://github.com/artefactual/archivematica/releases/tag/v1.13.2) and the [X3D validation package](https://www.web3d.org/specifications/x3d.all.validation.zip) were used to analyze, design, develop and test this script.

## Background

As part of the [NFDI4Culture](https://nfdi4culture.de/) initiative, efforts are underway to enhance the capabilities of open-source digital preservation software like Archivematica to identify, validate and preserve 3D file formats. This repository provides the **x3d_validator_for_archivematica** script to enable Extensible 3D (X3D) file validation in Archivematica, which is not supported by default in version 1.13.2, enhancing its 3D content preservation capabilities.

## Related projects

- [dae_validator_for_archivematica](https://github.com/JoergHeseler/dae_validator_for_archivematica)
- [gltf_validator_for_archivematica](https://github.com/JoergHeseler/gltf_validator_for_archivematica)
- [siegfried_falls_back_on_fido_identifier_for_archivematica](https://github.com/JoergHeseler/siegfried_falls_back_on_fido_identifier_for_archivematica)
- [stl_validator_for_archivematica](https://github.com/JoergHeseler/stl_validator_for_archivematica)

## Imprint

[NFDI4Culture](https://nfdi4culture.de/) – Consortium for Research Data on Material and Immaterial Cultural Heritage

NFDI4Culture is a consortium within the German [National Research Data Infrastructure (NFDI)](https://www.nfdi.de/).

Author: [Jörg Heseler](https://orcid.org/0000-0002-1497-627X)

This project is licensed under a [Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

NFDI4Culture is funded by the German Research Foundation (DFG) – Project number – [441958017](https://gepris.dfg.de/gepris/projekt/441958017).