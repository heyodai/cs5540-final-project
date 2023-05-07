# cs5540-final-project

## Building the project report

The project report is built using [Pandoc](http://pandoc.org/). The rough draft is stored in `report/report.md`. The final report is built using the `Dockerfile` in the `report` directory.

To build the report, run the following commands in the `report` directory:

```bash
docker build -t markdown-to-word .
docker run --rm -v $(pwd)/report:/app -w /app markdown-to-word
```
