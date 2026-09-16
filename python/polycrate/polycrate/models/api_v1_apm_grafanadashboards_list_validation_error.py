from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_apm_grafanadashboards_list_created_by_users_error_component import (
        ApiV1ApmGrafanadashboardsListCreatedByUsersErrorComponent,
    )
    from ..models.api_v1_apm_grafanadashboards_list_kind_error_component import (
        ApiV1ApmGrafanadashboardsListKindErrorComponent,
    )
    from ..models.api_v1_apm_grafanadashboards_list_name_exact_error_component import (
        ApiV1ApmGrafanadashboardsListNameExactErrorComponent,
    )
    from ..models.api_v1_apm_grafanadashboards_list_search_error_component import (
        ApiV1ApmGrafanadashboardsListSearchErrorComponent,
    )
    from ..models.api_v1_apm_grafanadashboards_list_source_uid_error_component import (
        ApiV1ApmGrafanadashboardsListSourceUidErrorComponent,
    )
    from ..models.api_v1_apm_grafanadashboards_list_state_error_component import (
        ApiV1ApmGrafanadashboardsListStateErrorComponent,
    )
    from ..models.api_v1_apm_grafanadashboards_list_state_not_error_component import (
        ApiV1ApmGrafanadashboardsListStateNotErrorComponent,
    )
    from ..models.api_v1_apm_grafanadashboards_list_time_range_error_component import (
        ApiV1ApmGrafanadashboardsListTimeRangeErrorComponent,
    )


T = TypeVar("T", bound="ApiV1ApmGrafanadashboardsListValidationError")


@_attrs_define
class ApiV1ApmGrafanadashboardsListValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1ApmGrafanadashboardsListCreatedByUsersErrorComponent |
            ApiV1ApmGrafanadashboardsListKindErrorComponent | ApiV1ApmGrafanadashboardsListNameExactErrorComponent |
            ApiV1ApmGrafanadashboardsListSearchErrorComponent | ApiV1ApmGrafanadashboardsListSourceUidErrorComponent |
            ApiV1ApmGrafanadashboardsListStateErrorComponent | ApiV1ApmGrafanadashboardsListStateNotErrorComponent |
            ApiV1ApmGrafanadashboardsListTimeRangeErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1ApmGrafanadashboardsListCreatedByUsersErrorComponent
        | ApiV1ApmGrafanadashboardsListKindErrorComponent
        | ApiV1ApmGrafanadashboardsListNameExactErrorComponent
        | ApiV1ApmGrafanadashboardsListSearchErrorComponent
        | ApiV1ApmGrafanadashboardsListSourceUidErrorComponent
        | ApiV1ApmGrafanadashboardsListStateErrorComponent
        | ApiV1ApmGrafanadashboardsListStateNotErrorComponent
        | ApiV1ApmGrafanadashboardsListTimeRangeErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_apm_grafanadashboards_list_created_by_users_error_component import (
            ApiV1ApmGrafanadashboardsListCreatedByUsersErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_apm_grafanadashboards_list_kind_error_component import (
            ApiV1ApmGrafanadashboardsListKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_apm_grafanadashboards_list_name_exact_error_component import (
            ApiV1ApmGrafanadashboardsListNameExactErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_apm_grafanadashboards_list_search_error_component import (
            ApiV1ApmGrafanadashboardsListSearchErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_apm_grafanadashboards_list_state_error_component import (
            ApiV1ApmGrafanadashboardsListStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_apm_grafanadashboards_list_state_not_error_component import (
            ApiV1ApmGrafanadashboardsListStateNotErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_apm_grafanadashboards_list_time_range_error_component import (
            ApiV1ApmGrafanadashboardsListTimeRangeErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1ApmGrafanadashboardsListSearchErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ApmGrafanadashboardsListTimeRangeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ApmGrafanadashboardsListStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ApmGrafanadashboardsListKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ApmGrafanadashboardsListCreatedByUsersErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ApmGrafanadashboardsListStateNotErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ApmGrafanadashboardsListNameExactErrorComponent):
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
        from ..models.api_v1_apm_grafanadashboards_list_created_by_users_error_component import (
            ApiV1ApmGrafanadashboardsListCreatedByUsersErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_apm_grafanadashboards_list_kind_error_component import (
            ApiV1ApmGrafanadashboardsListKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_apm_grafanadashboards_list_name_exact_error_component import (
            ApiV1ApmGrafanadashboardsListNameExactErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_apm_grafanadashboards_list_search_error_component import (
            ApiV1ApmGrafanadashboardsListSearchErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_apm_grafanadashboards_list_source_uid_error_component import (
            ApiV1ApmGrafanadashboardsListSourceUidErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_apm_grafanadashboards_list_state_error_component import (
            ApiV1ApmGrafanadashboardsListStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_apm_grafanadashboards_list_state_not_error_component import (
            ApiV1ApmGrafanadashboardsListStateNotErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_apm_grafanadashboards_list_time_range_error_component import (
            ApiV1ApmGrafanadashboardsListTimeRangeErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1ApmGrafanadashboardsListCreatedByUsersErrorComponent
                | ApiV1ApmGrafanadashboardsListKindErrorComponent
                | ApiV1ApmGrafanadashboardsListNameExactErrorComponent
                | ApiV1ApmGrafanadashboardsListSearchErrorComponent
                | ApiV1ApmGrafanadashboardsListSourceUidErrorComponent
                | ApiV1ApmGrafanadashboardsListStateErrorComponent
                | ApiV1ApmGrafanadashboardsListStateNotErrorComponent
                | ApiV1ApmGrafanadashboardsListTimeRangeErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_apm_grafanadashboards_list_error_type_0 = (
                        ApiV1ApmGrafanadashboardsListSearchErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_apm_grafanadashboards_list_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_apm_grafanadashboards_list_error_type_1 = (
                        ApiV1ApmGrafanadashboardsListTimeRangeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_apm_grafanadashboards_list_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_apm_grafanadashboards_list_error_type_2 = (
                        ApiV1ApmGrafanadashboardsListStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_apm_grafanadashboards_list_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_apm_grafanadashboards_list_error_type_3 = (
                        ApiV1ApmGrafanadashboardsListKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_apm_grafanadashboards_list_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_apm_grafanadashboards_list_error_type_4 = (
                        ApiV1ApmGrafanadashboardsListCreatedByUsersErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_apm_grafanadashboards_list_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_apm_grafanadashboards_list_error_type_5 = (
                        ApiV1ApmGrafanadashboardsListStateNotErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_apm_grafanadashboards_list_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_apm_grafanadashboards_list_error_type_6 = (
                        ApiV1ApmGrafanadashboardsListNameExactErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_apm_grafanadashboards_list_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_apm_grafanadashboards_list_error_type_7 = (
                    ApiV1ApmGrafanadashboardsListSourceUidErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_apm_grafanadashboards_list_error_type_7

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_apm_grafanadashboards_list_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_apm_grafanadashboards_list_validation_error.additional_properties = d
        return api_v1_apm_grafanadashboards_list_validation_error

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
