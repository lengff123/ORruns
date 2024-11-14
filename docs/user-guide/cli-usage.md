# Command Line Interface Guide

## Overview

ORruns provides a powerful CLI for managing experiments directly from the terminal.

## Basic Commands

### List Experiments
```bash
# List all experiments
orruns list

# List with detailed information
orruns list --detailed

# Filter experiments by pattern
orruns list --pattern "nsga*"
```

### View Experiment Information
```bash
# View experiment details
orruns info experiment_name

# View specific run details
orruns info experiment_name --run-id run_123
```

### Delete Experiments
```bash
# Delete an experiment
orruns delete experiment_name

# Force delete without confirmation
orruns delete experiment_name --force
```

## Advanced Features

### Experiment Comparison
```bash
# Compare multiple experiments
orruns compare exp1 exp2 --metric hypervolume

# Export comparison results
orruns compare exp1 exp2 --export report.pdf
```

### Configuration Management
```bash
# Set data directory
orruns config data-dir /path/to/data

# Show current configuration
orruns config show
```

### Artifact Management
```bash
# List artifacts
orruns artifacts list experiment_name

# Export artifacts
orruns artifacts export experiment_name --output ./exports
```

## Tips and Tricks

1. **Batch Operations**
   - Use wildcards for multiple experiments
   - Chain commands with pipes
   - Create command aliases

2. **Output Formatting**
   - JSON output for scripting
   - Pretty printing for readability
   - Custom format templates