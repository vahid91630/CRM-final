"""
Main application package initializer.
"""

# Optional: If you want to initialize logging, configs, or check envs
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)
logging.info("App package initialized.")
