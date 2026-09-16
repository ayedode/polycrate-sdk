from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_catalogue_apps_list_artifact_package_error_component import (
        ApiV1CatalogueAppsListArtifactPackageErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_list_created_at_error_component import (
        ApiV1CatalogueAppsListCreatedAtErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_list_created_by_component_error_component import (
        ApiV1CatalogueAppsListCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_list_created_by_users_error_component import (
        ApiV1CatalogueAppsListCreatedByUsersErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_list_kind_error_component import ApiV1CatalogueAppsListKindErrorComponent
    from ..models.api_v1_catalogue_apps_list_maintainer_error_component import (
        ApiV1CatalogueAppsListMaintainerErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_list_name_error_component import ApiV1CatalogueAppsListNameErrorComponent
    from ..models.api_v1_catalogue_apps_list_name_exact_error_component import (
        ApiV1CatalogueAppsListNameExactErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_list_scope_error_component import ApiV1CatalogueAppsListScopeErrorComponent
    from ..models.api_v1_catalogue_apps_list_search_error_component import ApiV1CatalogueAppsListSearchErrorComponent
    from ..models.api_v1_catalogue_apps_list_state_error_component import ApiV1CatalogueAppsListStateErrorComponent
    from ..models.api_v1_catalogue_apps_list_state_not_error_component import (
        ApiV1CatalogueAppsListStateNotErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_list_time_range_error_component import (
        ApiV1CatalogueAppsListTimeRangeErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_list_updated_at_error_component import (
        ApiV1CatalogueAppsListUpdatedAtErrorComponent,
    )


T = TypeVar("T", bound="ApiV1CatalogueAppsListValidationError")


@_attrs_define
class ApiV1CatalogueAppsListValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1CatalogueAppsListArtifactPackageErrorComponent | ApiV1CatalogueAppsListCreatedAtErrorComponent
            | ApiV1CatalogueAppsListCreatedByComponentErrorComponent | ApiV1CatalogueAppsListCreatedByUsersErrorComponent |
            ApiV1CatalogueAppsListKindErrorComponent | ApiV1CatalogueAppsListMaintainerErrorComponent |
            ApiV1CatalogueAppsListNameErrorComponent | ApiV1CatalogueAppsListNameExactErrorComponent |
            ApiV1CatalogueAppsListScopeErrorComponent | ApiV1CatalogueAppsListSearchErrorComponent |
            ApiV1CatalogueAppsListStateErrorComponent | ApiV1CatalogueAppsListStateNotErrorComponent |
            ApiV1CatalogueAppsListTimeRangeErrorComponent | ApiV1CatalogueAppsListUpdatedAtErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1CatalogueAppsListArtifactPackageErrorComponent
        | ApiV1CatalogueAppsListCreatedAtErrorComponent
        | ApiV1CatalogueAppsListCreatedByComponentErrorComponent
        | ApiV1CatalogueAppsListCreatedByUsersErrorComponent
        | ApiV1CatalogueAppsListKindErrorComponent
        | ApiV1CatalogueAppsListMaintainerErrorComponent
        | ApiV1CatalogueAppsListNameErrorComponent
        | ApiV1CatalogueAppsListNameExactErrorComponent
        | ApiV1CatalogueAppsListScopeErrorComponent
        | ApiV1CatalogueAppsListSearchErrorComponent
        | ApiV1CatalogueAppsListStateErrorComponent
        | ApiV1CatalogueAppsListStateNotErrorComponent
        | ApiV1CatalogueAppsListTimeRangeErrorComponent
        | ApiV1CatalogueAppsListUpdatedAtErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_catalogue_apps_list_artifact_package_error_component import (
            ApiV1CatalogueAppsListArtifactPackageErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_list_created_at_error_component import (
            ApiV1CatalogueAppsListCreatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_list_created_by_component_error_component import (
            ApiV1CatalogueAppsListCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_list_created_by_users_error_component import (
            ApiV1CatalogueAppsListCreatedByUsersErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_list_kind_error_component import (
            ApiV1CatalogueAppsListKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_list_maintainer_error_component import (
            ApiV1CatalogueAppsListMaintainerErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_list_name_error_component import (
            ApiV1CatalogueAppsListNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_list_scope_error_component import (
            ApiV1CatalogueAppsListScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_list_search_error_component import (
            ApiV1CatalogueAppsListSearchErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_list_state_error_component import (
            ApiV1CatalogueAppsListStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_list_state_not_error_component import (
            ApiV1CatalogueAppsListStateNotErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_list_time_range_error_component import (
            ApiV1CatalogueAppsListTimeRangeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_list_updated_at_error_component import (
            ApiV1CatalogueAppsListUpdatedAtErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1CatalogueAppsListSearchErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsListTimeRangeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsListStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsListKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsListCreatedByUsersErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsListCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsListNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsListCreatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsListUpdatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsListScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsListArtifactPackageErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsListMaintainerErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsListStateNotErrorComponent):
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
        from ..models.api_v1_catalogue_apps_list_artifact_package_error_component import (
            ApiV1CatalogueAppsListArtifactPackageErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_list_created_at_error_component import (
            ApiV1CatalogueAppsListCreatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_list_created_by_component_error_component import (
            ApiV1CatalogueAppsListCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_list_created_by_users_error_component import (
            ApiV1CatalogueAppsListCreatedByUsersErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_list_kind_error_component import (
            ApiV1CatalogueAppsListKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_list_maintainer_error_component import (
            ApiV1CatalogueAppsListMaintainerErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_list_name_error_component import (
            ApiV1CatalogueAppsListNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_list_name_exact_error_component import (
            ApiV1CatalogueAppsListNameExactErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_list_scope_error_component import (
            ApiV1CatalogueAppsListScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_list_search_error_component import (
            ApiV1CatalogueAppsListSearchErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_list_state_error_component import (
            ApiV1CatalogueAppsListStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_list_state_not_error_component import (
            ApiV1CatalogueAppsListStateNotErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_list_time_range_error_component import (
            ApiV1CatalogueAppsListTimeRangeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_list_updated_at_error_component import (
            ApiV1CatalogueAppsListUpdatedAtErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1CatalogueAppsListArtifactPackageErrorComponent
                | ApiV1CatalogueAppsListCreatedAtErrorComponent
                | ApiV1CatalogueAppsListCreatedByComponentErrorComponent
                | ApiV1CatalogueAppsListCreatedByUsersErrorComponent
                | ApiV1CatalogueAppsListKindErrorComponent
                | ApiV1CatalogueAppsListMaintainerErrorComponent
                | ApiV1CatalogueAppsListNameErrorComponent
                | ApiV1CatalogueAppsListNameExactErrorComponent
                | ApiV1CatalogueAppsListScopeErrorComponent
                | ApiV1CatalogueAppsListSearchErrorComponent
                | ApiV1CatalogueAppsListStateErrorComponent
                | ApiV1CatalogueAppsListStateNotErrorComponent
                | ApiV1CatalogueAppsListTimeRangeErrorComponent
                | ApiV1CatalogueAppsListUpdatedAtErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_list_error_type_0 = (
                        ApiV1CatalogueAppsListSearchErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_list_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_list_error_type_1 = (
                        ApiV1CatalogueAppsListTimeRangeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_list_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_list_error_type_2 = (
                        ApiV1CatalogueAppsListStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_list_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_list_error_type_3 = (
                        ApiV1CatalogueAppsListKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_list_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_list_error_type_4 = (
                        ApiV1CatalogueAppsListCreatedByUsersErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_list_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_list_error_type_5 = (
                        ApiV1CatalogueAppsListCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_list_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_list_error_type_6 = (
                        ApiV1CatalogueAppsListNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_list_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_list_error_type_7 = (
                        ApiV1CatalogueAppsListCreatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_list_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_list_error_type_8 = (
                        ApiV1CatalogueAppsListUpdatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_list_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_list_error_type_9 = (
                        ApiV1CatalogueAppsListScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_list_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_list_error_type_10 = (
                        ApiV1CatalogueAppsListArtifactPackageErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_list_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_list_error_type_11 = (
                        ApiV1CatalogueAppsListMaintainerErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_list_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_list_error_type_12 = (
                        ApiV1CatalogueAppsListStateNotErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_list_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_catalogue_apps_list_error_type_13 = (
                    ApiV1CatalogueAppsListNameExactErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_catalogue_apps_list_error_type_13

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_catalogue_apps_list_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_catalogue_apps_list_validation_error.additional_properties = d
        return api_v1_catalogue_apps_list_validation_error

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
