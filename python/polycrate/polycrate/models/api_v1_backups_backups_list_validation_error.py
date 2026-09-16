from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_backups_backups_list_backup_provider_app_error_component import (
        ApiV1BackupsBackupsListBackupProviderAppErrorComponent,
    )
    from ..models.api_v1_backups_backups_list_created_at_error_component import (
        ApiV1BackupsBackupsListCreatedAtErrorComponent,
    )
    from ..models.api_v1_backups_backups_list_created_by_component_error_component import (
        ApiV1BackupsBackupsListCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_backups_backups_list_created_by_users_error_component import (
        ApiV1BackupsBackupsListCreatedByUsersErrorComponent,
    )
    from ..models.api_v1_backups_backups_list_k8s_cluster_error_component import (
        ApiV1BackupsBackupsListK8SClusterErrorComponent,
    )
    from ..models.api_v1_backups_backups_list_kind_error_component import ApiV1BackupsBackupsListKindErrorComponent
    from ..models.api_v1_backups_backups_list_name_error_component import ApiV1BackupsBackupsListNameErrorComponent
    from ..models.api_v1_backups_backups_list_name_exact_error_component import (
        ApiV1BackupsBackupsListNameExactErrorComponent,
    )
    from ..models.api_v1_backups_backups_list_organizations_error_component import (
        ApiV1BackupsBackupsListOrganizationsErrorComponent,
    )
    from ..models.api_v1_backups_backups_list_provider_error_component import (
        ApiV1BackupsBackupsListProviderErrorComponent,
    )
    from ..models.api_v1_backups_backups_list_s3_bucket_error_component import (
        ApiV1BackupsBackupsListS3BucketErrorComponent,
    )
    from ..models.api_v1_backups_backups_list_schedule_error_component import (
        ApiV1BackupsBackupsListScheduleErrorComponent,
    )
    from ..models.api_v1_backups_backups_list_scope_error_component import ApiV1BackupsBackupsListScopeErrorComponent
    from ..models.api_v1_backups_backups_list_search_error_component import ApiV1BackupsBackupsListSearchErrorComponent
    from ..models.api_v1_backups_backups_list_source_namespace_error_component import (
        ApiV1BackupsBackupsListSourceNamespaceErrorComponent,
    )
    from ..models.api_v1_backups_backups_list_state_error_component import ApiV1BackupsBackupsListStateErrorComponent
    from ..models.api_v1_backups_backups_list_state_not_error_component import (
        ApiV1BackupsBackupsListStateNotErrorComponent,
    )
    from ..models.api_v1_backups_backups_list_status_error_component import ApiV1BackupsBackupsListStatusErrorComponent
    from ..models.api_v1_backups_backups_list_time_range_error_component import (
        ApiV1BackupsBackupsListTimeRangeErrorComponent,
    )
    from ..models.api_v1_backups_backups_list_updated_at_error_component import (
        ApiV1BackupsBackupsListUpdatedAtErrorComponent,
    )
    from ..models.api_v1_backups_backups_list_workspaces_error_component import (
        ApiV1BackupsBackupsListWorkspacesErrorComponent,
    )


T = TypeVar("T", bound="ApiV1BackupsBackupsListValidationError")


@_attrs_define
class ApiV1BackupsBackupsListValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1BackupsBackupsListBackupProviderAppErrorComponent |
            ApiV1BackupsBackupsListCreatedAtErrorComponent | ApiV1BackupsBackupsListCreatedByComponentErrorComponent |
            ApiV1BackupsBackupsListCreatedByUsersErrorComponent | ApiV1BackupsBackupsListK8SClusterErrorComponent |
            ApiV1BackupsBackupsListKindErrorComponent | ApiV1BackupsBackupsListNameErrorComponent |
            ApiV1BackupsBackupsListNameExactErrorComponent | ApiV1BackupsBackupsListOrganizationsErrorComponent |
            ApiV1BackupsBackupsListProviderErrorComponent | ApiV1BackupsBackupsListS3BucketErrorComponent |
            ApiV1BackupsBackupsListScheduleErrorComponent | ApiV1BackupsBackupsListScopeErrorComponent |
            ApiV1BackupsBackupsListSearchErrorComponent | ApiV1BackupsBackupsListSourceNamespaceErrorComponent |
            ApiV1BackupsBackupsListStateErrorComponent | ApiV1BackupsBackupsListStateNotErrorComponent |
            ApiV1BackupsBackupsListStatusErrorComponent | ApiV1BackupsBackupsListTimeRangeErrorComponent |
            ApiV1BackupsBackupsListUpdatedAtErrorComponent | ApiV1BackupsBackupsListWorkspacesErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1BackupsBackupsListBackupProviderAppErrorComponent
        | ApiV1BackupsBackupsListCreatedAtErrorComponent
        | ApiV1BackupsBackupsListCreatedByComponentErrorComponent
        | ApiV1BackupsBackupsListCreatedByUsersErrorComponent
        | ApiV1BackupsBackupsListK8SClusterErrorComponent
        | ApiV1BackupsBackupsListKindErrorComponent
        | ApiV1BackupsBackupsListNameErrorComponent
        | ApiV1BackupsBackupsListNameExactErrorComponent
        | ApiV1BackupsBackupsListOrganizationsErrorComponent
        | ApiV1BackupsBackupsListProviderErrorComponent
        | ApiV1BackupsBackupsListS3BucketErrorComponent
        | ApiV1BackupsBackupsListScheduleErrorComponent
        | ApiV1BackupsBackupsListScopeErrorComponent
        | ApiV1BackupsBackupsListSearchErrorComponent
        | ApiV1BackupsBackupsListSourceNamespaceErrorComponent
        | ApiV1BackupsBackupsListStateErrorComponent
        | ApiV1BackupsBackupsListStateNotErrorComponent
        | ApiV1BackupsBackupsListStatusErrorComponent
        | ApiV1BackupsBackupsListTimeRangeErrorComponent
        | ApiV1BackupsBackupsListUpdatedAtErrorComponent
        | ApiV1BackupsBackupsListWorkspacesErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_backups_backups_list_backup_provider_app_error_component import (
            ApiV1BackupsBackupsListBackupProviderAppErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_list_created_at_error_component import (
            ApiV1BackupsBackupsListCreatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_list_created_by_component_error_component import (
            ApiV1BackupsBackupsListCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_list_created_by_users_error_component import (
            ApiV1BackupsBackupsListCreatedByUsersErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_list_k8s_cluster_error_component import (
            ApiV1BackupsBackupsListK8SClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_list_kind_error_component import (
            ApiV1BackupsBackupsListKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_list_name_error_component import (
            ApiV1BackupsBackupsListNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_list_name_exact_error_component import (
            ApiV1BackupsBackupsListNameExactErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_list_organizations_error_component import (
            ApiV1BackupsBackupsListOrganizationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_list_provider_error_component import (
            ApiV1BackupsBackupsListProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_list_s3_bucket_error_component import (
            ApiV1BackupsBackupsListS3BucketErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_list_scope_error_component import (
            ApiV1BackupsBackupsListScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_list_search_error_component import (
            ApiV1BackupsBackupsListSearchErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_list_source_namespace_error_component import (
            ApiV1BackupsBackupsListSourceNamespaceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_list_state_error_component import (
            ApiV1BackupsBackupsListStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_list_state_not_error_component import (
            ApiV1BackupsBackupsListStateNotErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_list_status_error_component import (
            ApiV1BackupsBackupsListStatusErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_list_time_range_error_component import (
            ApiV1BackupsBackupsListTimeRangeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_list_updated_at_error_component import (
            ApiV1BackupsBackupsListUpdatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_list_workspaces_error_component import (
            ApiV1BackupsBackupsListWorkspacesErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1BackupsBackupsListSearchErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsListTimeRangeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsListOrganizationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsListWorkspacesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsListStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsListKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsListCreatedByUsersErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsListCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsListNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsListCreatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsListUpdatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsListScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsListStateNotErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsListNameExactErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsListProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsListSourceNamespaceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsListStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsListK8SClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsListBackupProviderAppErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupsListS3BucketErrorComponent):
                errors_item = errors_item_data.to_dict()
            else:
                errors_item = errors_item_data.to_dict()

            errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "errors": errors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_v1_backups_backups_list_backup_provider_app_error_component import (
            ApiV1BackupsBackupsListBackupProviderAppErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_list_created_at_error_component import (
            ApiV1BackupsBackupsListCreatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_list_created_by_component_error_component import (
            ApiV1BackupsBackupsListCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_list_created_by_users_error_component import (
            ApiV1BackupsBackupsListCreatedByUsersErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_list_k8s_cluster_error_component import (
            ApiV1BackupsBackupsListK8SClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_list_kind_error_component import (
            ApiV1BackupsBackupsListKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_list_name_error_component import (
            ApiV1BackupsBackupsListNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_list_name_exact_error_component import (
            ApiV1BackupsBackupsListNameExactErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_list_organizations_error_component import (
            ApiV1BackupsBackupsListOrganizationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_list_provider_error_component import (
            ApiV1BackupsBackupsListProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_list_s3_bucket_error_component import (
            ApiV1BackupsBackupsListS3BucketErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_list_schedule_error_component import (
            ApiV1BackupsBackupsListScheduleErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_list_scope_error_component import (
            ApiV1BackupsBackupsListScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_list_search_error_component import (
            ApiV1BackupsBackupsListSearchErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_list_source_namespace_error_component import (
            ApiV1BackupsBackupsListSourceNamespaceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_list_state_error_component import (
            ApiV1BackupsBackupsListStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_list_state_not_error_component import (
            ApiV1BackupsBackupsListStateNotErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_list_status_error_component import (
            ApiV1BackupsBackupsListStatusErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_list_time_range_error_component import (
            ApiV1BackupsBackupsListTimeRangeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_list_updated_at_error_component import (
            ApiV1BackupsBackupsListUpdatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backups_list_workspaces_error_component import (
            ApiV1BackupsBackupsListWorkspacesErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1BackupsBackupsListBackupProviderAppErrorComponent
                | ApiV1BackupsBackupsListCreatedAtErrorComponent
                | ApiV1BackupsBackupsListCreatedByComponentErrorComponent
                | ApiV1BackupsBackupsListCreatedByUsersErrorComponent
                | ApiV1BackupsBackupsListK8SClusterErrorComponent
                | ApiV1BackupsBackupsListKindErrorComponent
                | ApiV1BackupsBackupsListNameErrorComponent
                | ApiV1BackupsBackupsListNameExactErrorComponent
                | ApiV1BackupsBackupsListOrganizationsErrorComponent
                | ApiV1BackupsBackupsListProviderErrorComponent
                | ApiV1BackupsBackupsListS3BucketErrorComponent
                | ApiV1BackupsBackupsListScheduleErrorComponent
                | ApiV1BackupsBackupsListScopeErrorComponent
                | ApiV1BackupsBackupsListSearchErrorComponent
                | ApiV1BackupsBackupsListSourceNamespaceErrorComponent
                | ApiV1BackupsBackupsListStateErrorComponent
                | ApiV1BackupsBackupsListStateNotErrorComponent
                | ApiV1BackupsBackupsListStatusErrorComponent
                | ApiV1BackupsBackupsListTimeRangeErrorComponent
                | ApiV1BackupsBackupsListUpdatedAtErrorComponent
                | ApiV1BackupsBackupsListWorkspacesErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_list_error_type_0 = (
                        ApiV1BackupsBackupsListSearchErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_list_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_list_error_type_1 = (
                        ApiV1BackupsBackupsListTimeRangeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_list_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_list_error_type_2 = (
                        ApiV1BackupsBackupsListOrganizationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_list_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_list_error_type_3 = (
                        ApiV1BackupsBackupsListWorkspacesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_list_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_list_error_type_4 = (
                        ApiV1BackupsBackupsListStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_list_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_list_error_type_5 = (
                        ApiV1BackupsBackupsListKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_list_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_list_error_type_6 = (
                        ApiV1BackupsBackupsListCreatedByUsersErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_list_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_list_error_type_7 = (
                        ApiV1BackupsBackupsListCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_list_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_list_error_type_8 = (
                        ApiV1BackupsBackupsListNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_list_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_list_error_type_9 = (
                        ApiV1BackupsBackupsListCreatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_list_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_list_error_type_10 = (
                        ApiV1BackupsBackupsListUpdatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_list_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_list_error_type_11 = (
                        ApiV1BackupsBackupsListScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_list_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_list_error_type_12 = (
                        ApiV1BackupsBackupsListStateNotErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_list_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_list_error_type_13 = (
                        ApiV1BackupsBackupsListNameExactErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_list_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_list_error_type_14 = (
                        ApiV1BackupsBackupsListProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_list_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_list_error_type_15 = (
                        ApiV1BackupsBackupsListSourceNamespaceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_list_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_list_error_type_16 = (
                        ApiV1BackupsBackupsListStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_list_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_list_error_type_17 = (
                        ApiV1BackupsBackupsListK8SClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_list_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_list_error_type_18 = (
                        ApiV1BackupsBackupsListBackupProviderAppErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_list_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backups_list_error_type_19 = (
                        ApiV1BackupsBackupsListS3BucketErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backups_list_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_backups_backups_list_error_type_20 = (
                    ApiV1BackupsBackupsListScheduleErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_backups_backups_list_error_type_20

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_backups_backups_list_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_backups_backups_list_validation_error.additional_properties = d
        return api_v1_backups_backups_list_validation_error

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
