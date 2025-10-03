from datetime import datetime

from pydantic import BaseModel, Field, HttpUrl


class Resource(BaseModel):
    """
    Pydantic model for resource data.

    Represents a design pattern resource with metadata.
    """

    resource_url: HttpUrl = Field(
        ...,
        description="URL of the resource",
        examples=["https://example.com/design-pattern"],
    )

    md_file_name: str = Field(
        ...,
        description="Name of the markdown file",
        min_length=1,
        examples=["001_singleton_design_pattern.md"],
    )

    date: datetime = Field(
        ...,
        description="Date when the resource was created/processed",
        examples=["2024-01-15T10:30:00Z"],
    )

    design_pattern_name: str = Field(
        ...,
        description="Name of the design pattern",
        min_length=1,
        examples=["Singleton Pattern", "Factory Method Pattern"],
    )

    creator_name: str = Field(
        ...,
        description="Name of the creator",
        min_length=1,
        examples=["John Doe", "Jane Smith"],
    )

    class Config:
        """Pydantic configuration."""

        json_encoders = {datetime: lambda v: v.isoformat(), HttpUrl: lambda v: str(v)}
        schema_extra = {
            "example": {
                "resource_url": "https://www.geeksforgeeks.org/system-design-singleton-design-pattern/",
                "md_file_name": "001_www_geeksforgeeks_org_system_design_singleton_design_pattern.md",
                "date": "2024-01-15T10:30:00Z",
                "design_pattern_name": "Singleton Design Pattern",
                "creator_name": "System Administrator",
            }
        }
