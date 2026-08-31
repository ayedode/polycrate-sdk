from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_blocks_list_artifact_packages_error_component import (
        ApiV1BlocksListArtifactPackagesErrorComponent,
    )
    from ..models.api_v1_blocks_list_checksum_error_component import ApiV1BlocksListChecksumErrorComponent
    from ..models.api_v1_blocks_list_created_by_users_error_component import ApiV1BlocksListCreatedByUsersErrorComponent
    from ..models.api_v1_blocks_list_from_block_error_component import ApiV1BlocksListFromBlockErrorComponent
    from ..models.api_v1_blocks_list_kind_error_component import ApiV1BlocksListKindErrorComponent
    from ..models.api_v1_blocks_list_name_exact_error_component import ApiV1BlocksListNameExactErrorComponent
    from ..models.api_v1_blocks_list_organizations_error_component import ApiV1BlocksListOrganizationsErrorComponent
    from ..models.api_v1_blocks_list_registry_url_error_component import ApiV1BlocksListRegistryUrlErrorComponent
    from ..models.api_v1_blocks_list_search_error_component import ApiV1BlocksListSearchErrorComponent
    from ..models.api_v1_blocks_list_state_error_component import ApiV1BlocksListStateErrorComponent
    from ..models.api_v1_blocks_list_state_not_error_component import ApiV1BlocksListStateNotErrorComponent
    from ..models.api_v1_blocks_list_template_block_error_component import ApiV1BlocksListTemplateBlockErrorComponent
    from ..models.api_v1_blocks_list_time_range_error_component import ApiV1BlocksListTimeRangeErrorComponent
    from ..models.api_v1_blocks_list_version_error_component import ApiV1BlocksListVersionErrorComponent
    from ..models.api_v1_blocks_list_workspaces_error_component import ApiV1BlocksListWorkspacesErrorComponent


T = TypeVar("T", bound="ApiV1BlocksListValidationError")


@_attrs_define
class ApiV1BlocksListValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1BlocksListArtifactPackagesErrorComponent | ApiV1BlocksListChecksumErrorComponent |
            ApiV1BlocksListCreatedByUsersErrorComponent | ApiV1BlocksListFromBlockErrorComponent |
            ApiV1BlocksListKindErrorComponent | ApiV1BlocksListNameExactErrorComponent |
            ApiV1BlocksListOrganizationsErrorComponent | ApiV1BlocksListRegistryUrlErrorComponent |
            ApiV1BlocksListSearchErrorComponent | ApiV1BlocksListStateErrorComponent | ApiV1BlocksListStateNotErrorComponent
            | ApiV1BlocksListTemplateBlockErrorComponent | ApiV1BlocksListTimeRangeErrorComponent |
            ApiV1BlocksListVersionErrorComponent | ApiV1BlocksListWorkspacesErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1BlocksListArtifactPackagesErrorComponent
        | ApiV1BlocksListChecksumErrorComponent
        | ApiV1BlocksListCreatedByUsersErrorComponent
        | ApiV1BlocksListFromBlockErrorComponent
        | ApiV1BlocksListKindErrorComponent
        | ApiV1BlocksListNameExactErrorComponent
        | ApiV1BlocksListOrganizationsErrorComponent
        | ApiV1BlocksListRegistryUrlErrorComponent
        | ApiV1BlocksListSearchErrorComponent
        | ApiV1BlocksListStateErrorComponent
        | ApiV1BlocksListStateNotErrorComponent
        | ApiV1BlocksListTemplateBlockErrorComponent
        | ApiV1BlocksListTimeRangeErrorComponent
        | ApiV1BlocksListVersionErrorComponent
        | ApiV1BlocksListWorkspacesErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_blocks_list_artifact_packages_error_component import (
            ApiV1BlocksListArtifactPackagesErrorComponent,
        )
        from ..models.api_v1_blocks_list_checksum_error_component import ApiV1BlocksListChecksumErrorComponent
        from ..models.api_v1_blocks_list_created_by_users_error_component import (
            ApiV1BlocksListCreatedByUsersErrorComponent,
        )
        from ..models.api_v1_blocks_list_from_block_error_component import ApiV1BlocksListFromBlockErrorComponent
        from ..models.api_v1_blocks_list_kind_error_component import ApiV1BlocksListKindErrorComponent
        from ..models.api_v1_blocks_list_name_exact_error_component import ApiV1BlocksListNameExactErrorComponent
        from ..models.api_v1_blocks_list_organizations_error_component import ApiV1BlocksListOrganizationsErrorComponent
        from ..models.api_v1_blocks_list_search_error_component import ApiV1BlocksListSearchErrorComponent
        from ..models.api_v1_blocks_list_state_error_component import ApiV1BlocksListStateErrorComponent
        from ..models.api_v1_blocks_list_state_not_error_component import ApiV1BlocksListStateNotErrorComponent
        from ..models.api_v1_blocks_list_template_block_error_component import (
            ApiV1BlocksListTemplateBlockErrorComponent,
        )
        from ..models.api_v1_blocks_list_time_range_error_component import ApiV1BlocksListTimeRangeErrorComponent
        from ..models.api_v1_blocks_list_version_error_component import ApiV1BlocksListVersionErrorComponent
        from ..models.api_v1_blocks_list_workspaces_error_component import ApiV1BlocksListWorkspacesErrorComponent

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1BlocksListSearchErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksListTimeRangeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksListOrganizationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksListWorkspacesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksListStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksListKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksListCreatedByUsersErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksListTemplateBlockErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksListFromBlockErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksListVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksListChecksumErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksListArtifactPackagesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksListStateNotErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksListNameExactErrorComponent):
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
        from ..models.api_v1_blocks_list_artifact_packages_error_component import (
            ApiV1BlocksListArtifactPackagesErrorComponent,
        )
        from ..models.api_v1_blocks_list_checksum_error_component import ApiV1BlocksListChecksumErrorComponent
        from ..models.api_v1_blocks_list_created_by_users_error_component import (
            ApiV1BlocksListCreatedByUsersErrorComponent,
        )
        from ..models.api_v1_blocks_list_from_block_error_component import ApiV1BlocksListFromBlockErrorComponent
        from ..models.api_v1_blocks_list_kind_error_component import ApiV1BlocksListKindErrorComponent
        from ..models.api_v1_blocks_list_name_exact_error_component import ApiV1BlocksListNameExactErrorComponent
        from ..models.api_v1_blocks_list_organizations_error_component import ApiV1BlocksListOrganizationsErrorComponent
        from ..models.api_v1_blocks_list_registry_url_error_component import ApiV1BlocksListRegistryUrlErrorComponent
        from ..models.api_v1_blocks_list_search_error_component import ApiV1BlocksListSearchErrorComponent
        from ..models.api_v1_blocks_list_state_error_component import ApiV1BlocksListStateErrorComponent
        from ..models.api_v1_blocks_list_state_not_error_component import ApiV1BlocksListStateNotErrorComponent
        from ..models.api_v1_blocks_list_template_block_error_component import (
            ApiV1BlocksListTemplateBlockErrorComponent,
        )
        from ..models.api_v1_blocks_list_time_range_error_component import ApiV1BlocksListTimeRangeErrorComponent
        from ..models.api_v1_blocks_list_version_error_component import ApiV1BlocksListVersionErrorComponent
        from ..models.api_v1_blocks_list_workspaces_error_component import ApiV1BlocksListWorkspacesErrorComponent

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1BlocksListArtifactPackagesErrorComponent
                | ApiV1BlocksListChecksumErrorComponent
                | ApiV1BlocksListCreatedByUsersErrorComponent
                | ApiV1BlocksListFromBlockErrorComponent
                | ApiV1BlocksListKindErrorComponent
                | ApiV1BlocksListNameExactErrorComponent
                | ApiV1BlocksListOrganizationsErrorComponent
                | ApiV1BlocksListRegistryUrlErrorComponent
                | ApiV1BlocksListSearchErrorComponent
                | ApiV1BlocksListStateErrorComponent
                | ApiV1BlocksListStateNotErrorComponent
                | ApiV1BlocksListTemplateBlockErrorComponent
                | ApiV1BlocksListTimeRangeErrorComponent
                | ApiV1BlocksListVersionErrorComponent
                | ApiV1BlocksListWorkspacesErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_list_error_type_0 = ApiV1BlocksListSearchErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_blocks_list_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_list_error_type_1 = (
                        ApiV1BlocksListTimeRangeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_list_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_list_error_type_2 = (
                        ApiV1BlocksListOrganizationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_list_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_list_error_type_3 = (
                        ApiV1BlocksListWorkspacesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_list_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_list_error_type_4 = ApiV1BlocksListStateErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_blocks_list_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_list_error_type_5 = ApiV1BlocksListKindErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_blocks_list_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_list_error_type_6 = (
                        ApiV1BlocksListCreatedByUsersErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_list_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_list_error_type_7 = (
                        ApiV1BlocksListTemplateBlockErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_list_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_list_error_type_8 = (
                        ApiV1BlocksListFromBlockErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_list_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_list_error_type_9 = ApiV1BlocksListVersionErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_blocks_list_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_list_error_type_10 = (
                        ApiV1BlocksListChecksumErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_list_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_list_error_type_11 = (
                        ApiV1BlocksListArtifactPackagesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_list_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_list_error_type_12 = (
                        ApiV1BlocksListStateNotErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_list_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_list_error_type_13 = (
                        ApiV1BlocksListNameExactErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_list_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_blocks_list_error_type_14 = ApiV1BlocksListRegistryUrlErrorComponent.from_dict(
                    data
                )

                return componentsschemas_api_v1_blocks_list_error_type_14

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_blocks_list_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_blocks_list_validation_error.additional_properties = d
        return api_v1_blocks_list_validation_error

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
