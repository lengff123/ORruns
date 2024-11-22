# Command Line Interface Guide

## Overview

ORruns provides a command-line interface (CLI) for managing experiments and analyzing results.

## Basic Commands

### List Experiments

```bash
# List last 10 experiments
orruns list

# List all experiments
orruns list --all

# Filter experiments by pattern
orruns list --pattern "tsp_*"

# Show detailed information
orruns list --detailed
```

### View Experiment Details

```bash
# View experiment summary
orruns info experiment_name

# View specific run details
orruns info experiment_name --run-id run_20240315_123456

# Export metrics to CSV
orruns info experiment_name --export metrics.csv
```

### Export Data

```bash
# Export experiment metrics
orruns export experiment_name --metrics objective,time,gap

# Export artifacts
orruns export experiment_name --run-id run_20240315_123456 --output ./exports

# Export specific artifact types
orruns export experiment_name --artifacts figures,data
```

### Query Experiments

```bash
# Query by parameters
orruns query --params "solver=cplex,n_cities>20"

# Query by metrics
orruns query --metrics "objective<1000,gap<0.01"

# Sort results
orruns query --sort-by "metrics.objective" --ascending
```

### Clean Up

```bash
# Delete specific experiment
orruns delete experiment_name

# Delete old experiments
orruns clean --days 30

# Force delete without confirmation
orruns delete experiment_name --force
```

## Advanced Usage

### Comparing Experiments

```bash
# Compare multiple experiments
orruns compare exp1 exp2 --metrics objective,time

# Export comparison results
orruns compare exp1 exp2 --export comparison.csv

# Visualize comparison
orruns compare exp1 exp2 --plot
```

### Configuration

```bash
# Show current configuration
orruns config show

# Set data directory
orruns config set data_dir /path/to/data

# Reset configuration
orruns config reset
```

## Examples

### Analyzing Experiment Results

```bash
# Get experiment history
orruns history tsp_experiment --metrics objective

# Plot convergence
orruns plot tsp_experiment --metric objective --type line

# Export statistics
orruns stats tsp_experiment --export stats.csv
```

### Batch Operations

```bash
# Export multiple experiments
orruns export "tsp_*" --metrics objective,time

# Clean up old experiments
orruns clean --pattern "test_*" --days 7

# Compare multiple runs
orruns compare exp1 exp2 exp3 --metrics objective
```

## Tips

1. **Using Patterns**
   - Use `*` for wildcard matching
   - Use `?` for single character matching
   - Patterns are case-sensitive

2. **Output Formats**
   - Default: Human-readable format
   - `--json`: JSON output
   - `--csv`: CSV format
   - `--quiet`: Minimal output

3. **Error Handling**
   - Use `--debug` for detailed error messages
   - Use `--force` to skip confirmations
   - Use `--retry` for network operations

## Environment Variables

- `ORRUNS_DATA_DIR`: Default data directory
- `ORRUNS_CONFIG`: Custom config file path
- `ORRUNS_LOG_LEVEL`: Logging level

## See Also

- [API Reference](../api-reference/cli.md)
- [Configuration Guide](configuration.md)
- [Examples](../examples/cli-examples.md)