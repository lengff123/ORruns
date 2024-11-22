# Command Line Interface (CLI)

ORruns provides a command-line interface for managing experiments and analyzing results.

## Basic Usage

```bash
orruns [command] [options]
```

## Commands

### List Experiments

List all experiments or filter by pattern:

```bash
# List last 10 experiments
orruns list

# List with custom limit
orruns list --last 20

# Filter by name pattern
orruns list --pattern "tsp_*"
```

### Get Experiment Details

View details of a specific experiment:

```bash
# Get experiment overview
orruns get experiment_name

# Get specific run details
orruns get experiment_name --run-id run_20240315_123456
```

### Query Experiments

Search experiments with filters:

```bash
# Filter by parameters
orruns query --param "solver=cplex" --param "threads>=4"

# Filter by metrics
orruns query --metric "objective<100" --metric "gap<=0.01"

# Sort results
orruns query --sort-by "metrics.objective" --ascending
```

### Export Results

Export experiment data:

```bash
# Export to CSV
orruns export experiment_name --format csv --output results.csv

# Export specific metrics
orruns export experiment_name --metrics objective,time,gap

# Export artifacts
orruns export experiment_name --artifacts --output ./exported
```

### Delete Experiments

Remove experiments or specific runs:

```bash
# Delete experiment
orruns delete experiment_name

# Delete specific run
orruns delete experiment_name --run-id run_20240315_123456

# Clean old experiments
orruns clean --days 30
```

## Common Options

| Option | Description |
|--------|-------------|
| `--base-dir` | Custom base directory for experiments |
| `--format` | Output format (json, csv, table) |
| `--quiet` | Suppress output messages |
| `--verbose` | Show detailed information |

## Examples

### Compare Multiple Experiments

```bash
# Compare metrics across experiments
orruns compare exp1 exp2 --metrics objective,time

# Export comparison to CSV
orruns compare exp1 exp2 --format csv --output comparison.csv
```

### Analyze Experiment History

```bash
# View experiment history
orruns history experiment_name

# Export history to CSV
orruns history experiment_name --format csv --output history.csv
```

### Launch Dashboard

```bash
# Start visualization dashboard
orruns dashboard

# Custom port
orruns dashboard --port 8080
```

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `ORRUNS_BASE_DIR` | Base directory for experiments | `./orruns_experiments` |
| `ORRUNS_LOG_LEVEL` | Logging level | `INFO` |

## Configuration

Create `.orrunsrc` in your home directory or project root:

```yaml
base_dir: /path/to/experiments
default_format: table
log_level: INFO
```

## Error Handling

Common error messages and solutions:

| Error | Solution |
|-------|----------|
| `Experiment not found` | Check experiment name and base directory |
| `Invalid filter format` | Use correct operator (=, >, <, >=, <=) |
| `Permission denied` | Check directory permissions |

## Advanced Usage

### Custom Filters

```bash
# Complex parameter filters
orruns query \
  --param "solver=cplex" \
  --param "threads>=4" \
  --param "method=barrier" \
  --sort-by "metrics.time"
```

### Batch Operations

```bash
# Export multiple experiments
orruns export exp1 exp2 exp3 --metrics objective,time

# Delete multiple experiments
orruns delete exp1 exp2 exp3 --force
```

### Format Options

```bash
# Pretty table output
orruns list --format table

# JSON output for scripting
orruns list --format json

# CSV for data analysis
orruns list --format csv
```