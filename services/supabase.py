from typing import Any, Dict, List, Optional

from configs.supabase import supabase


class SupabaseService:
    """
    Service class for Supabase operations.
    Provides methods to interact with Supabase database.
    """

    def __init__(self):
        """Initialize the Supabase service with the configured client."""
        self.client = supabase.client

    def add_resource(self, table_name: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Add a new resource to the specified table.

        :param table_name: Name of the table to insert data into
        :param data: Dictionary containing the data to insert
        :return: Response from Supabase with inserted data
        :raises Exception: If the operation fails
        """
        try:
            response = self.client.table(table_name).insert(data).execute()
            return response.data[0] if response.data else {}
        except Exception as e:
            raise Exception(f"Failed to add resource to {table_name}: {str(e)}")

    def get_resource(
        self, table_name: str, resource_id: str
    ) -> Optional[Dict[str, Any]]:
        """
        Get a specific resource by ID.

        :param table_name: Name of the table to query
        :param resource_id: ID of the resource to retrieve
        :return: Resource data if found, None otherwise
        """
        try:
            response = (
                self.client.table(table_name)
                .select("*")
                .eq("id", resource_id)
                .execute()
            )
            return response.data[0] if response.data else None
        except Exception as e:
            print(f"Error retrieving resource from {table_name}: {str(e)}")
            return None

    def get_all_resources(self, table_name: str) -> List[Dict[str, Any]]:
        """
        Get all resources from a table.

        :param table_name: Name of the table to query
        :return: List of all resources in the table
        """
        try:
            response = self.client.table(table_name).select("*").execute()
            return response.data or []
        except Exception as e:
            print(f"Error retrieving all resources from {table_name}: {str(e)}")
            return []

    def update_resource(
        self, table_name: str, resource_id: str, data: Dict[str, Any]
    ) -> Optional[Dict[str, Any]]:
        """
        Update a specific resource.

        :param table_name: Name of the table to update
        :param resource_id: ID of the resource to update
        :param data: Dictionary containing the updated data
        :return: Updated resource data if successful, None otherwise
        """
        try:
            response = (
                self.client.table(table_name)
                .update(data)
                .eq("id", resource_id)
                .execute()
            )
            return response.data[0] if response.data else None
        except Exception as e:
            print(f"Error updating resource in {table_name}: {str(e)}")
            return None

    def delete_resource(self, table_name: str, resource_id: str) -> bool:
        """
        Delete a specific resource.

        :param table_name: Name of the table to delete from
        :param resource_id: ID of the resource to delete
        :return: True if deletion was successful, False otherwise
        """
        try:
            response = (
                self.client.table(table_name).delete().eq("id", resource_id).execute()
            )
            return len(response.data) > 0
        except Exception as e:
            print(f"Error deleting resource from {table_name}: {str(e)}")
            return False

    def query_resources(
        self, table_name: str, filters: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """
        Query resources with custom filters.

        :param table_name: Name of the table to query
        :param filters: Dictionary containing filter conditions
        :return: List of resources matching the filters
        """
        try:
            query = self.client.table(table_name).select("*")

            for column, value in filters.items():
                query = query.eq(column, value)

            response = query.execute()
            return response.data or []
        except Exception as e:
            print(f"Error querying resources from {table_name}: {str(e)}")
            return []


# Create a singleton instance for easy import
supabase_service = SupabaseService()
