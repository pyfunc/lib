from setuptools import setup

# This overrides automatic license file handling
setup(
    # Explicitly disable license_files to prevent the problematic metadata
    license_files=(),
)