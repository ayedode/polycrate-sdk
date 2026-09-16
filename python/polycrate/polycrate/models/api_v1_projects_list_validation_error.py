from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_projects_list_created_by_users_error_component import (
        ApiV1ProjectsListCreatedByUsersErrorComponent,
    )
    from ..models.api_v1_projects_list_end_date_from_error_component import ApiV1ProjectsListEndDateFromErrorComponent
    from ..models.api_v1_projects_list_end_date_to_error_component import ApiV1ProjectsListEndDateToErrorComponent
    from ..models.api_v1_projects_list_kind_error_component import ApiV1ProjectsListKindErrorComponent
    from ..models.api_v1_projects_list_name_exact_error_component import ApiV1ProjectsListNameExactErrorComponent
    from ..models.api_v1_projects_list_organizations_error_component import ApiV1ProjectsListOrganizationsErrorComponent
    from ..models.api_v1_projects_list_product_error_component import ApiV1ProjectsListProductErrorComponent
    from ..models.api_v1_projects_list_search_error_component import ApiV1ProjectsListSearchErrorComponent
    from ..models.api_v1_projects_list_start_date_from_error_component import (
        ApiV1ProjectsListStartDateFromErrorComponent,
    )
    from ..models.api_v1_projects_list_start_date_to_error_component import ApiV1ProjectsListStartDateToErrorComponent
    from ..models.api_v1_projects_list_state_error_component import ApiV1ProjectsListStateErrorComponent
    from ..models.api_v1_projects_list_state_not_error_component import ApiV1ProjectsListStateNotErrorComponent
    from ..models.api_v1_projects_list_time_range_error_component import ApiV1ProjectsListTimeRangeErrorComponent


T = TypeVar("T", bound="ApiV1ProjectsListValidationError")


@_attrs_define
class ApiV1ProjectsListValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1ProjectsListCreatedByUsersErrorComponent | ApiV1ProjectsListEndDateFromErrorComponent |
            ApiV1ProjectsListEndDateToErrorComponent | ApiV1ProjectsListKindErrorComponent |
            ApiV1ProjectsListNameExactErrorComponent | ApiV1ProjectsListOrganizationsErrorComponent |
            ApiV1ProjectsListProductErrorComponent | ApiV1ProjectsListSearchErrorComponent |
            ApiV1ProjectsListStartDateFromErrorComponent | ApiV1ProjectsListStartDateToErrorComponent |
            ApiV1ProjectsListStateErrorComponent | ApiV1ProjectsListStateNotErrorComponent |
            ApiV1ProjectsListTimeRangeErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1ProjectsListCreatedByUsersErrorComponent
        | ApiV1ProjectsListEndDateFromErrorComponent
        | ApiV1ProjectsListEndDateToErrorComponent
        | ApiV1ProjectsListKindErrorComponent
        | ApiV1ProjectsListNameExactErrorComponent
        | ApiV1ProjectsListOrganizationsErrorComponent
        | ApiV1ProjectsListProductErrorComponent
        | ApiV1ProjectsListSearchErrorComponent
        | ApiV1ProjectsListStartDateFromErrorComponent
        | ApiV1ProjectsListStartDateToErrorComponent
        | ApiV1ProjectsListStateErrorComponent
        | ApiV1ProjectsListStateNotErrorComponent
        | ApiV1ProjectsListTimeRangeErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_projects_list_created_by_users_error_component import (
            ApiV1ProjectsListCreatedByUsersErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_list_end_date_from_error_component import (
            ApiV1ProjectsListEndDateFromErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_list_end_date_to_error_component import (
            ApiV1ProjectsListEndDateToErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_list_kind_error_component import (
            ApiV1ProjectsListKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_list_organizations_error_component import (
            ApiV1ProjectsListOrganizationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_list_product_error_component import (
            ApiV1ProjectsListProductErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_list_search_error_component import (
            ApiV1ProjectsListSearchErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_list_start_date_from_error_component import (
            ApiV1ProjectsListStartDateFromErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_list_start_date_to_error_component import (
            ApiV1ProjectsListStartDateToErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_list_state_error_component import (
            ApiV1ProjectsListStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_list_state_not_error_component import (
            ApiV1ProjectsListStateNotErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_list_time_range_error_component import (
            ApiV1ProjectsListTimeRangeErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1ProjectsListSearchErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsListTimeRangeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsListOrganizationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsListStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsListKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsListCreatedByUsersErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsListStartDateFromErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsListStartDateToErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsListEndDateFromErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsListEndDateToErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsListProductErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsListStateNotErrorComponent):
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
        from ..models.api_v1_projects_list_created_by_users_error_component import (
            ApiV1ProjectsListCreatedByUsersErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_list_end_date_from_error_component import (
            ApiV1ProjectsListEndDateFromErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_list_end_date_to_error_component import (
            ApiV1ProjectsListEndDateToErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_list_kind_error_component import (
            ApiV1ProjectsListKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_list_name_exact_error_component import (
            ApiV1ProjectsListNameExactErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_list_organizations_error_component import (
            ApiV1ProjectsListOrganizationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_list_product_error_component import (
            ApiV1ProjectsListProductErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_list_search_error_component import (
            ApiV1ProjectsListSearchErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_list_start_date_from_error_component import (
            ApiV1ProjectsListStartDateFromErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_list_start_date_to_error_component import (
            ApiV1ProjectsListStartDateToErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_list_state_error_component import (
            ApiV1ProjectsListStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_list_state_not_error_component import (
            ApiV1ProjectsListStateNotErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_list_time_range_error_component import (
            ApiV1ProjectsListTimeRangeErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1ProjectsListCreatedByUsersErrorComponent
                | ApiV1ProjectsListEndDateFromErrorComponent
                | ApiV1ProjectsListEndDateToErrorComponent
                | ApiV1ProjectsListKindErrorComponent
                | ApiV1ProjectsListNameExactErrorComponent
                | ApiV1ProjectsListOrganizationsErrorComponent
                | ApiV1ProjectsListProductErrorComponent
                | ApiV1ProjectsListSearchErrorComponent
                | ApiV1ProjectsListStartDateFromErrorComponent
                | ApiV1ProjectsListStartDateToErrorComponent
                | ApiV1ProjectsListStateErrorComponent
                | ApiV1ProjectsListStateNotErrorComponent
                | ApiV1ProjectsListTimeRangeErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_list_error_type_0 = (
                        ApiV1ProjectsListSearchErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_list_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_list_error_type_1 = (
                        ApiV1ProjectsListTimeRangeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_list_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_list_error_type_2 = (
                        ApiV1ProjectsListOrganizationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_list_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_list_error_type_3 = (
                        ApiV1ProjectsListStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_list_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_list_error_type_4 = ApiV1ProjectsListKindErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_projects_list_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_list_error_type_5 = (
                        ApiV1ProjectsListCreatedByUsersErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_list_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_list_error_type_6 = (
                        ApiV1ProjectsListStartDateFromErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_list_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_list_error_type_7 = (
                        ApiV1ProjectsListStartDateToErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_list_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_list_error_type_8 = (
                        ApiV1ProjectsListEndDateFromErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_list_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_list_error_type_9 = (
                        ApiV1ProjectsListEndDateToErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_list_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_list_error_type_10 = (
                        ApiV1ProjectsListProductErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_list_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_list_error_type_11 = (
                        ApiV1ProjectsListStateNotErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_list_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_projects_list_error_type_12 = (
                    ApiV1ProjectsListNameExactErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_projects_list_error_type_12

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_projects_list_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_projects_list_validation_error.additional_properties = d
        return api_v1_projects_list_validation_error

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
