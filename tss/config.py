"""Configuration loader for application."""
import os

from prometheus_client import CollectorRegistry

REGISTRY = CollectorRegistry()


# pylint: disable=too-few-public-methods,simplifiable-if-expression
class Config:
    """Configuration for app."""

    NAMESPACE = os.getenv("NAMESPACE")
    PROMETHEUS_PUSH_GATEWAY = os.getenv("PROMETHEUS_PUSH_GATEWAY")
