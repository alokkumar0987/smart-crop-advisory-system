import os

structure = {
    "smart-crop-advisory-system": {
        "backend": {
            "app": {
                "api": {
                    "endpoints": [
                        "advisory.py",
                        "chat.py",
                        "farmer_profiles.py",
                        "images.py",
                        "weather_market.py",
                    ],
                    "dependencies.py": None,
                },
                "core": [
                    "config.py",
                    "security.py",
                    "logger.py",
                ],
                "agents": [
                    "base_agent.py",
                    "supervisor_agent.py",
                    "stt_agent.py",
                    "intent_agent.py",
                    "ner_agent.py",
                    "vision_agent.py",
                    "retrieval_agent.py",
                    "external_api_agent.py",
                    "llm_agent.py",
                ],
                "models": {
                    "pydantic": [
                        "advisory.py",
                        "chat.py",
                        "user.py",
                    ],
                    "orm": [
                        "advisory.py",
                        "farmer_profile.py",
                        "user.py",
                    ],
                },
                "services": {
                    "external_apis": [
                        "weather_service.py",
                        "market_service.py",
                        "govt_schemes_service.py",
                    ],
                    "cache.py": None,
                    "database.py": None,
                    "knowledge_base.py": None,
                    "notification.py": None,
                },
                "utils": [
                    "helpers.py",
                    "validators.py",
                ],
                "main.py": None,
            },
            "data": {
                "knowledge_base": [
                    "crop_protocols",
                    "pest_management",
                    "fertilizer_guides",
                    "govt_schemes",
                ],
                "ml_models": [
                    "intent_classifier",
                    "ner_model",
                    "disease_detection",
                ],
            },
            "tests": [
                "api",
                "agents",
                "services",
                "utils",
            ],
            "alembic": None,
            "requirements.txt": None,
            "Dockerfile": None,
        },
        "frontend": {
            "public": None,
            "src": {
                "components": [
                    "advisory",
                    "image_upload",
                    "ui",
                    "voice_input",
                ],
                "hooks": None,
                "pages": None,
                "services": [
                    "api.js",
                    "offlineSync.js",
                    "tts.js",
                    "notifications.js",
                ],
                "utils": [
                    "indexedDB.js",
                    "i18n.js",
                ],
                "styles": None,
            },
            "tests": None,
            "package.json": None,
            "Dockerfile": None,
        },
        "ml_models": {
            "training_notebooks": None,
            "scripts": None,
            "data": {
                "images": [
                    "train",
                    "val",
                ],
                "text": None,
            },
            "requirements.txt": None,
            "utils": None,
        },
        "infrastructure": {
            "docker-compose.yml": None,
            "kubernetes": None,
            "nginx": None,
            "scripts": [
                "init_vector_db.py",
                "deploy.sh",
            ],
        },
        "docs": [
            "api.md",
            "architecture.md",
            "user_guide.md",
            "changelog.md",
        ],
        ".env.example": None,
    }
}

def create_structure(base_path, struct):
    if isinstance(struct, dict):
        for k, v in struct.items():
            dir_path = os.path.join(base_path, k)
            if v is None:
                # Create file
                open(dir_path, 'a').close()
            elif isinstance(v, list):
                # Create folder and files inside it
                os.makedirs(dir_path, exist_ok=True)
                for item in v:
                    if isinstance(item, str):
                        path = os.path.join(dir_path, item)
                        if "." in item:
                            # It's a file
                            open(path, 'a').close()
                        else:
                            # It's a folder
                            os.makedirs(path, exist_ok=True)
                    elif isinstance(item, dict):
                        create_structure(dir_path, item)
            elif isinstance(v, dict):
                os.makedirs(dir_path, exist_ok=True)
                create_structure(dir_path, v)
    elif isinstance(struct, list):
        for item in struct:
            path = os.path.join(base_path, item)
            if "." in item:
                open(path, 'a').close()
            else:
                os.makedirs(path, exist_ok=True)

if __name__ == "__main__":
    root_dir = "."
    create_structure(root_dir, structure)
    print("Folder structure created successfully!")