# Installation Guide

## Prerequisites

Before installing ORruns, ensure you have:
- Python 3.8 or later
- pip (Python package installer)

## Installation Methods

### From PyPI (Recommended)
```bash
pip install orruns
```

### From Source
```bash
git clone https://github.com/lengff123/ORruns.git
cd ORruns
pip install -e .
```

## Verify Installation

To verify that ORruns is installed correctly:
```python
import orruns
print(orruns.__version__)
```

## Dependencies

ORruns automatically installs the following key dependencies:
- numpy
- pandas
- matplotlib
- [other dependencies]

## Platform Support

ORruns supports:
- Windows 10 or later
- macOS 10.14+
- Linux (most modern distributions)

## Troubleshooting

If you encounter any installation issues:

1. Ensure your Python version is compatible:
```bash
python --version
```

2. Update pip to the latest version:
```bash
pip install --upgrade pip
```

3. If you face any issues, please [report them](git clone https://github.com/lengff123/ORruns/issues)