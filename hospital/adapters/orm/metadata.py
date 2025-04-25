from sqlalchemy.orm import registry

mapper_registry = registry()
mapper_metadata = mapper_registry.metadata