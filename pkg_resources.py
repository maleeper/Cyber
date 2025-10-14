"""Minimal pkg_resources replacement for environments without setuptools."""
from __future__ import annotations

from dataclasses import dataclass
from importlib import metadata


class DistributionNotFound(Exception):
    """Raised when the requested package metadata cannot be located."""


@dataclass
class _Distribution:
    name: str
    version: str


def get_distribution(package_name: str) -> _Distribution:
    """Return distribution metadata for ``package_name`` using importlib.metadata."""
    try:
        package_version = metadata.version(package_name)
    except metadata.PackageNotFoundError as exc:  # type: ignore[attr-defined]
        raise DistributionNotFound(package_name) from exc

    return _Distribution(name=package_name, version=package_version)
