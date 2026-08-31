from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_credentials_list_api_user_error_component import ApiV1CredentialsListApiUserErrorComponent
    from ..models.api_v1_credentials_list_created_at_error_component import ApiV1CredentialsListCreatedAtErrorComponent
    from ..models.api_v1_credentials_list_created_by_component_error_component import (
        ApiV1CredentialsListCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_credentials_list_created_by_users_error_component import (
        ApiV1CredentialsListCreatedByUsersErrorComponent,
    )
    from ..models.api_v1_credentials_list_k8s_clusters_error_component import (
        ApiV1CredentialsListK8SClustersErrorComponent,
    )
    from ..models.api_v1_credentials_list_kind_error_component import ApiV1CredentialsListKindErrorComponent
    from ..models.api_v1_credentials_list_name_error_component import ApiV1CredentialsListNameErrorComponent
    from ..models.api_v1_credentials_list_name_exact_error_component import ApiV1CredentialsListNameExactErrorComponent
    from ..models.api_v1_credentials_list_organizations_error_component import (
        ApiV1CredentialsListOrganizationsErrorComponent,
    )
    from ..models.api_v1_credentials_list_s3_clusters_error_component import (
        ApiV1CredentialsListS3ClustersErrorComponent,
    )
    from ..models.api_v1_credentials_list_scope_error_component import ApiV1CredentialsListScopeErrorComponent
    from ..models.api_v1_credentials_list_search_error_component import ApiV1CredentialsListSearchErrorComponent
    from ..models.api_v1_credentials_list_state_error_component import ApiV1CredentialsListStateErrorComponent
    from ..models.api_v1_credentials_list_state_not_error_component import ApiV1CredentialsListStateNotErrorComponent
    from ..models.api_v1_credentials_list_time_range_error_component import ApiV1CredentialsListTimeRangeErrorComponent
    from ..models.api_v1_credentials_list_updated_at_error_component import ApiV1CredentialsListUpdatedAtErrorComponent
    from ..models.api_v1_credentials_list_workspaces_error_component import ApiV1CredentialsListWorkspacesErrorComponent


T = TypeVar("T", bound="ApiV1CredentialsListValidationError")


@_attrs_define
class ApiV1CredentialsListValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1CredentialsListApiUserErrorComponent | ApiV1CredentialsListCreatedAtErrorComponent |
            ApiV1CredentialsListCreatedByComponentErrorComponent | ApiV1CredentialsListCreatedByUsersErrorComponent |
            ApiV1CredentialsListK8SClustersErrorComponent | ApiV1CredentialsListKindErrorComponent |
            ApiV1CredentialsListNameErrorComponent | ApiV1CredentialsListNameExactErrorComponent |
            ApiV1CredentialsListOrganizationsErrorComponent | ApiV1CredentialsListS3ClustersErrorComponent |
            ApiV1CredentialsListScopeErrorComponent | ApiV1CredentialsListSearchErrorComponent |
            ApiV1CredentialsListStateErrorComponent | ApiV1CredentialsListStateNotErrorComponent |
            ApiV1CredentialsListTimeRangeErrorComponent | ApiV1CredentialsListUpdatedAtErrorComponent |
            ApiV1CredentialsListWorkspacesErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1CredentialsListApiUserErrorComponent
        | ApiV1CredentialsListCreatedAtErrorComponent
        | ApiV1CredentialsListCreatedByComponentErrorComponent
        | ApiV1CredentialsListCreatedByUsersErrorComponent
        | ApiV1CredentialsListK8SClustersErrorComponent
        | ApiV1CredentialsListKindErrorComponent
        | ApiV1CredentialsListNameErrorComponent
        | ApiV1CredentialsListNameExactErrorComponent
        | ApiV1CredentialsListOrganizationsErrorComponent
        | ApiV1CredentialsListS3ClustersErrorComponent
        | ApiV1CredentialsListScopeErrorComponent
        | ApiV1CredentialsListSearchErrorComponent
        | ApiV1CredentialsListStateErrorComponent
        | ApiV1CredentialsListStateNotErrorComponent
        | ApiV1CredentialsListTimeRangeErrorComponent
        | ApiV1CredentialsListUpdatedAtErrorComponent
        | ApiV1CredentialsListWorkspacesErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_credentials_list_api_user_error_component import ApiV1CredentialsListApiUserErrorComponent
        from ..models.api_v1_credentials_list_created_at_error_component import (
            ApiV1CredentialsListCreatedAtErrorComponent,
        )
        from ..models.api_v1_credentials_list_created_by_component_error_component import (
            ApiV1CredentialsListCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_credentials_list_created_by_users_error_component import (
            ApiV1CredentialsListCreatedByUsersErrorComponent,
        )
        from ..models.api_v1_credentials_list_k8s_clusters_error_component import (
            ApiV1CredentialsListK8SClustersErrorComponent,
        )
        from ..models.api_v1_credentials_list_kind_error_component import ApiV1CredentialsListKindErrorComponent
        from ..models.api_v1_credentials_list_name_error_component import ApiV1CredentialsListNameErrorComponent
        from ..models.api_v1_credentials_list_organizations_error_component import (
            ApiV1CredentialsListOrganizationsErrorComponent,
        )
        from ..models.api_v1_credentials_list_s3_clusters_error_component import (
            ApiV1CredentialsListS3ClustersErrorComponent,
        )
        from ..models.api_v1_credentials_list_scope_error_component import ApiV1CredentialsListScopeErrorComponent
        from ..models.api_v1_credentials_list_search_error_component import ApiV1CredentialsListSearchErrorComponent
        from ..models.api_v1_credentials_list_state_error_component import ApiV1CredentialsListStateErrorComponent
        from ..models.api_v1_credentials_list_state_not_error_component import (
            ApiV1CredentialsListStateNotErrorComponent,
        )
        from ..models.api_v1_credentials_list_time_range_error_component import (
            ApiV1CredentialsListTimeRangeErrorComponent,
        )
        from ..models.api_v1_credentials_list_updated_at_error_component import (
            ApiV1CredentialsListUpdatedAtErrorComponent,
        )
        from ..models.api_v1_credentials_list_workspaces_error_component import (
            ApiV1CredentialsListWorkspacesErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1CredentialsListSearchErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsListTimeRangeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsListOrganizationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsListWorkspacesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsListStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsListKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsListCreatedByUsersErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsListCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsListNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsListCreatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsListUpdatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsListScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsListApiUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsListK8SClustersErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsListS3ClustersErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsListStateNotErrorComponent):
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
        from ..models.api_v1_credentials_list_api_user_error_component import ApiV1CredentialsListApiUserErrorComponent
        from ..models.api_v1_credentials_list_created_at_error_component import (
            ApiV1CredentialsListCreatedAtErrorComponent,
        )
        from ..models.api_v1_credentials_list_created_by_component_error_component import (
            ApiV1CredentialsListCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_credentials_list_created_by_users_error_component import (
            ApiV1CredentialsListCreatedByUsersErrorComponent,
        )
        from ..models.api_v1_credentials_list_k8s_clusters_error_component import (
            ApiV1CredentialsListK8SClustersErrorComponent,
        )
        from ..models.api_v1_credentials_list_kind_error_component import ApiV1CredentialsListKindErrorComponent
        from ..models.api_v1_credentials_list_name_error_component import ApiV1CredentialsListNameErrorComponent
        from ..models.api_v1_credentials_list_name_exact_error_component import (
            ApiV1CredentialsListNameExactErrorComponent,
        )
        from ..models.api_v1_credentials_list_organizations_error_component import (
            ApiV1CredentialsListOrganizationsErrorComponent,
        )
        from ..models.api_v1_credentials_list_s3_clusters_error_component import (
            ApiV1CredentialsListS3ClustersErrorComponent,
        )
        from ..models.api_v1_credentials_list_scope_error_component import ApiV1CredentialsListScopeErrorComponent
        from ..models.api_v1_credentials_list_search_error_component import ApiV1CredentialsListSearchErrorComponent
        from ..models.api_v1_credentials_list_state_error_component import ApiV1CredentialsListStateErrorComponent
        from ..models.api_v1_credentials_list_state_not_error_component import (
            ApiV1CredentialsListStateNotErrorComponent,
        )
        from ..models.api_v1_credentials_list_time_range_error_component import (
            ApiV1CredentialsListTimeRangeErrorComponent,
        )
        from ..models.api_v1_credentials_list_updated_at_error_component import (
            ApiV1CredentialsListUpdatedAtErrorComponent,
        )
        from ..models.api_v1_credentials_list_workspaces_error_component import (
            ApiV1CredentialsListWorkspacesErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1CredentialsListApiUserErrorComponent
                | ApiV1CredentialsListCreatedAtErrorComponent
                | ApiV1CredentialsListCreatedByComponentErrorComponent
                | ApiV1CredentialsListCreatedByUsersErrorComponent
                | ApiV1CredentialsListK8SClustersErrorComponent
                | ApiV1CredentialsListKindErrorComponent
                | ApiV1CredentialsListNameErrorComponent
                | ApiV1CredentialsListNameExactErrorComponent
                | ApiV1CredentialsListOrganizationsErrorComponent
                | ApiV1CredentialsListS3ClustersErrorComponent
                | ApiV1CredentialsListScopeErrorComponent
                | ApiV1CredentialsListSearchErrorComponent
                | ApiV1CredentialsListStateErrorComponent
                | ApiV1CredentialsListStateNotErrorComponent
                | ApiV1CredentialsListTimeRangeErrorComponent
                | ApiV1CredentialsListUpdatedAtErrorComponent
                | ApiV1CredentialsListWorkspacesErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_list_error_type_0 = (
                        ApiV1CredentialsListSearchErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_list_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_list_error_type_1 = (
                        ApiV1CredentialsListTimeRangeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_list_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_list_error_type_2 = (
                        ApiV1CredentialsListOrganizationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_list_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_list_error_type_3 = (
                        ApiV1CredentialsListWorkspacesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_list_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_list_error_type_4 = (
                        ApiV1CredentialsListStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_list_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_list_error_type_5 = (
                        ApiV1CredentialsListKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_list_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_list_error_type_6 = (
                        ApiV1CredentialsListCreatedByUsersErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_list_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_list_error_type_7 = (
                        ApiV1CredentialsListCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_list_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_list_error_type_8 = (
                        ApiV1CredentialsListNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_list_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_list_error_type_9 = (
                        ApiV1CredentialsListCreatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_list_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_list_error_type_10 = (
                        ApiV1CredentialsListUpdatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_list_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_list_error_type_11 = (
                        ApiV1CredentialsListScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_list_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_list_error_type_12 = (
                        ApiV1CredentialsListApiUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_list_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_list_error_type_13 = (
                        ApiV1CredentialsListK8SClustersErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_list_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_list_error_type_14 = (
                        ApiV1CredentialsListS3ClustersErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_list_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_list_error_type_15 = (
                        ApiV1CredentialsListStateNotErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_list_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_credentials_list_error_type_16 = (
                    ApiV1CredentialsListNameExactErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_credentials_list_error_type_16

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_credentials_list_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_credentials_list_validation_error.additional_properties = d
        return api_v1_credentials_list_validation_error

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
