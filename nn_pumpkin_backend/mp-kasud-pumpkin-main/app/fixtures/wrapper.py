import json

class FixturesWrapper:

    def __init__(self):
        self._fixtures_path = "app/fixtures/data"

        self.config_router__get__config_id: dict = self.load_fixture_from_data("config_router.get.config_id.json", convert_to_json=True)
        self.config_router__get: dict | list = self.load_fixture_from_data("config_router.get.json", convert_to_json=True)
        self.config_router__get__list_user_settings: dict = self.load_fixture_from_data("config_router.get.list_user_settings.json", convert_to_json=True)
        self.config_router__post__check_version: dict = self.load_fixture_from_data("config_router.post.check_version.json", convert_to_json=True)
        self.config_router__post__user_settings: dict = self.load_fixture_from_data("config_router.post.user_settings.json", convert_to_json=True)

        self.auth_router__post__login: dict = self.load_fixture_from_data("auth_router.post.login.json", convert_to_json=True)
        self.auth_router__post__logout: dict = self.load_fixture_from_data("auth_router.post.logout.json", convert_to_json=True)

        self.catalog_router__post__fetch_catalogs_by_user: dict | list = self.load_fixture_from_data("catalog_router.post.fetch_catalogs_by_user.json", convert_to_json=True)
        self.catalog_router__get__get_content_by_type__calendar_deadline_days: dict | list = self.load_fixture_from_data("catalog_router.post.content.calendar_deadline_days.json", convert_to_json=True)
        self.catalog_router__get__get_content_by_type__calendar_off_days: dict | list = self.load_fixture_from_data("catalog_router.post.content.calendar_off_days.json", convert_to_json=True)
        self.catalog_router__get__get_content_by_type__document_types: dict | list = self.load_fixture_from_data("catalog_router.post.content.document_types.json", convert_to_json=True)
        self.catalog_router__get__get_content_by_type__task_types: dict | list = self.load_fixture_from_data("catalog_router.post.content.task_types.json", convert_to_json=True)
        self.catalog_router__get__get_content_by_type__users: dict | list = self.load_fixture_from_data("catalog_router.post.content.users.json", convert_to_json=True)

        self.sync_router__post__archive_documents: dict = self.load_fixture_from_data("sync_router.post.archive_documents.json", convert_to_json=True)
        self.sync_router__post__favorite_documents: dict = self.load_fixture_from_data("sync_router.post.favorite_documents.json", convert_to_json=True)
        self.sync_router__post__default_sync: dict = self.load_fixture_from_data("sync_router.post.default_sync.json", convert_to_json=True)
        self.sync_router__post__tasks: dict = self.load_fixture_from_data("sync_router.post.tasks.json", convert_to_json=True)
        self.sync_router__post__tasks__not_required: dict = self.load_fixture_from_data("sync_router.post.tasks.not_required.json", convert_to_json=True)

        self.sync_router__post__content: dict = self.load_fixture_from_data("sync_router.post.content.json", convert_to_json=True)
        self.sync_router__post__content_optional: dict = self.load_fixture_from_data("sync_router.post.content_optional.json", convert_to_json=True)

        self.commands_router__post__decisions: dict = self.load_fixture_from_data("commands_router.post.decisions.json", convert_to_json=True)

    def load_fixture_from_data(self, name: str, convert_to_json: bool = False) -> dict | str:
        with open(f"{self._fixtures_path}/{name}", "r") as file:
            raw = file.read()

        if convert_to_json:
            return json.loads(raw)

        return raw

fixtures_container = FixturesWrapper()