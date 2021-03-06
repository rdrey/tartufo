import pathlib
from typing import Tuple

import click

from tartufo import types, util
from tartufo.scanner import GitPreCommitScanner


@click.command("pre-commit")
@click.pass_obj
@click.pass_context
def main(
    ctx: click.Context, options: types.GlobalOptions
) -> Tuple[str, GitPreCommitScanner]:
    """Scan staged changes in a pre-commit hook."""
    # Assume that the current working directory is the appropriate git repo
    repo_path = pathlib.Path.cwd()
    scanner = None
    try:
        scanner = GitPreCommitScanner(options, str(repo_path))
        scanner.scan()
    except types.ScanException as exc:
        util.fail(str(exc), ctx)
    return (str(repo_path), scanner)  # type: ignore
