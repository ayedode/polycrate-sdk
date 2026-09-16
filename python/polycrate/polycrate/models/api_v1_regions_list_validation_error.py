from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_regions_list_created_by_users_error_component import (
        ApiV1RegionsListCreatedByUsersErrorComponent,
    )
    from ..models.api_v1_regions_list_kind_error_component import ApiV1RegionsListKindErrorComponent
    from ..models.api_v1_regions_list_name_exact_error_component import ApiV1RegionsListNameExactErrorComponent
    from ..models.api_v1_regions_list_organizations_error_component import ApiV1RegionsListOrganizationsErrorComponent
    from ..models.api_v1_regions_list_platform_features_error_component import (
        ApiV1RegionsListPlatformFeaturesErrorComponent,
    )
    from ..models.api_v1_regions_list_search_error_component import ApiV1RegionsListSearchErrorComponent
    from ..models.api_v1_regions_list_state_error_component import ApiV1RegionsListStateErrorComponent
    from ..models.api_v1_regions_list_state_not_error_component import ApiV1RegionsListStateNotErrorComponent
    from ..models.api_v1_regions_list_time_range_error_component import ApiV1RegionsListTimeRangeErrorComponent
    from ..models.api_v1_regions_list_workspaces_error_component import ApiV1RegionsListWorkspacesErrorComponent


T = TypeVar("T", bound="ApiV1RegionsListValidationError")


@_attrs_define
class ApiV1RegionsListValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1RegionsListCreatedByUsersErrorComponent | ApiV1RegionsListKindErrorComponent |
            ApiV1RegionsListNameExactErrorComponent | ApiV1RegionsListOrganizationsErrorComponent |
            ApiV1RegionsListPlatformFeaturesErrorComponent | ApiV1RegionsListSearchErrorComponent |
            ApiV1RegionsListStateErrorComponent | ApiV1RegionsListStateNotErrorComponent |
            ApiV1RegionsListTimeRangeErrorComponent | ApiV1RegionsListWorkspacesErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1RegionsListCreatedByUsersErrorComponent
        | ApiV1RegionsListKindErrorComponent
        | ApiV1RegionsListNameExactErrorComponent
        | ApiV1RegionsListOrganizationsErrorComponent
        | ApiV1RegionsListPlatformFeaturesErrorComponent
        | ApiV1RegionsListSearchErrorComponent
        | ApiV1RegionsListStateErrorComponent
        | ApiV1RegionsListStateNotErrorComponent
        | ApiV1RegionsListTimeRangeErrorComponent
        | ApiV1RegionsListWorkspacesErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_regions_list_created_by_users_error_component import (
            ApiV1RegionsListCreatedByUsersErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_list_kind_error_component import (
            ApiV1RegionsListKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_list_organizations_error_component import (
            ApiV1RegionsListOrganizationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_list_platform_features_error_component import (
            ApiV1RegionsListPlatformFeaturesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_list_search_error_component import (
            ApiV1RegionsListSearchErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_list_state_error_component import (
            ApiV1RegionsListStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_list_state_not_error_component import (
            ApiV1RegionsListStateNotErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_list_time_range_error_component import (
            ApiV1RegionsListTimeRangeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_list_workspaces_error_component import (
            ApiV1RegionsListWorkspacesErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1RegionsListSearchErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsListTimeRangeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsListOrganizationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsListWorkspacesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsListStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsListKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsListCreatedByUsersErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsListPlatformFeaturesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsListStateNotErrorComponent):
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
        from ..models.api_v1_regions_list_created_by_users_error_component import (
            ApiV1RegionsListCreatedByUsersErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_list_kind_error_component import (
            ApiV1RegionsListKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_list_name_exact_error_component import (
            ApiV1RegionsListNameExactErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_list_organizations_error_component import (
            ApiV1RegionsListOrganizationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_list_platform_features_error_component import (
            ApiV1RegionsListPlatformFeaturesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_list_search_error_component import (
            ApiV1RegionsListSearchErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_list_state_error_component import (
            ApiV1RegionsListStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_list_state_not_error_component import (
            ApiV1RegionsListStateNotErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_list_time_range_error_component import (
            ApiV1RegionsListTimeRangeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_list_workspaces_error_component import (
            ApiV1RegionsListWorkspacesErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1RegionsListCreatedByUsersErrorComponent
                | ApiV1RegionsListKindErrorComponent
                | ApiV1RegionsListNameExactErrorComponent
                | ApiV1RegionsListOrganizationsErrorComponent
                | ApiV1RegionsListPlatformFeaturesErrorComponent
                | ApiV1RegionsListSearchErrorComponent
                | ApiV1RegionsListStateErrorComponent
                | ApiV1RegionsListStateNotErrorComponent
                | ApiV1RegionsListTimeRangeErrorComponent
                | ApiV1RegionsListWorkspacesErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_list_error_type_0 = ApiV1RegionsListSearchErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_regions_list_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_list_error_type_1 = (
                        ApiV1RegionsListTimeRangeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_list_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_list_error_type_2 = (
                        ApiV1RegionsListOrganizationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_list_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_list_error_type_3 = (
                        ApiV1RegionsListWorkspacesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_list_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_list_error_type_4 = ApiV1RegionsListStateErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_regions_list_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_list_error_type_5 = ApiV1RegionsListKindErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_regions_list_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_list_error_type_6 = (
                        ApiV1RegionsListCreatedByUsersErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_list_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_list_error_type_7 = (
                        ApiV1RegionsListPlatformFeaturesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_list_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_list_error_type_8 = (
                        ApiV1RegionsListStateNotErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_list_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_regions_list_error_type_9 = ApiV1RegionsListNameExactErrorComponent.from_dict(
                    data
                )

                return componentsschemas_api_v1_regions_list_error_type_9

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_regions_list_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_regions_list_validation_error.additional_properties = d
        return api_v1_regions_list_validation_error

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
