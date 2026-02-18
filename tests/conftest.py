import pytest
import sys
from pathlib import Path

# Add parent directory to path to resolve imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from clients.tableau_client import TableauClient


@pytest.fixture(scope="session")
def tableau_client():
    client = TableauClient()
    with client.sign_in():
        yield client.server


@pytest.fixture
def base_url():
    return (
        "https://public.tableau.com"  # Replace with your actual Tableau server URL
    )
