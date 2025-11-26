import os

from dotenv import load_dotenv
from supabase import Client, create_client

load_dotenv()


class SupabaseConnector:
    def __init__(self, url: str, key: str):
        """
        Initialize the Supabase client.

        :param url: The Supabase project URL.
        :param key: The Supabase API key.
        """
        self.url = url
        self.key = key
        self.client: Client = create_client(self.url, self.key)


supabase = SupabaseConnector(
    url=os.getenv("SUPABASE_URL"), key=os.getenv("SUPABASE_KEY")
)
