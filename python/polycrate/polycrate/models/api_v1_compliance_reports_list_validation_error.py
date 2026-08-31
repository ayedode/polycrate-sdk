from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_compliance_reports_list_created_by_users_error_component import (
        ApiV1ComplianceReportsListCreatedByUsersErrorComponent,
    )
    from ..models.api_v1_compliance_reports_list_framework_refs_error_component import (
        ApiV1ComplianceReportsListFrameworkRefsErrorComponent,
    )
    from ..models.api_v1_compliance_reports_list_kind_error_component import (
        ApiV1ComplianceReportsListKindErrorComponent,
    )
    from ..models.api_v1_compliance_reports_list_name_exact_error_component import (
        ApiV1ComplianceReportsListNameExactErrorComponent,
    )
    from ..models.api_v1_compliance_reports_list_organizations_error_component import (
        ApiV1ComplianceReportsListOrganizationsErrorComponent,
    )
    from ..models.api_v1_compliance_reports_list_period_end_error_component import (
        ApiV1ComplianceReportsListPeriodEndErrorComponent,
    )
    from ..models.api_v1_compliance_reports_list_period_end_gte_error_component import (
        ApiV1ComplianceReportsListPeriodEndGteErrorComponent,
    )
    from ..models.api_v1_compliance_reports_list_period_start_error_component import (
        ApiV1ComplianceReportsListPeriodStartErrorComponent,
    )
    from ..models.api_v1_compliance_reports_list_period_start_lte_error_component import (
        ApiV1ComplianceReportsListPeriodStartLteErrorComponent,
    )
    from ..models.api_v1_compliance_reports_list_search_error_component import (
        ApiV1ComplianceReportsListSearchErrorComponent,
    )
    from ..models.api_v1_compliance_reports_list_state_error_component import (
        ApiV1ComplianceReportsListStateErrorComponent,
    )
    from ..models.api_v1_compliance_reports_list_state_not_error_component import (
        ApiV1ComplianceReportsListStateNotErrorComponent,
    )
    from ..models.api_v1_compliance_reports_list_status_error_component import (
        ApiV1ComplianceReportsListStatusErrorComponent,
    )
    from ..models.api_v1_compliance_reports_list_time_range_error_component import (
        ApiV1ComplianceReportsListTimeRangeErrorComponent,
    )


T = TypeVar("T", bound="ApiV1ComplianceReportsListValidationError")


@_attrs_define
class ApiV1ComplianceReportsListValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1ComplianceReportsListCreatedByUsersErrorComponent |
            ApiV1ComplianceReportsListFrameworkRefsErrorComponent | ApiV1ComplianceReportsListKindErrorComponent |
            ApiV1ComplianceReportsListNameExactErrorComponent | ApiV1ComplianceReportsListOrganizationsErrorComponent |
            ApiV1ComplianceReportsListPeriodEndErrorComponent | ApiV1ComplianceReportsListPeriodEndGteErrorComponent |
            ApiV1ComplianceReportsListPeriodStartErrorComponent | ApiV1ComplianceReportsListPeriodStartLteErrorComponent |
            ApiV1ComplianceReportsListSearchErrorComponent | ApiV1ComplianceReportsListStateErrorComponent |
            ApiV1ComplianceReportsListStateNotErrorComponent | ApiV1ComplianceReportsListStatusErrorComponent |
            ApiV1ComplianceReportsListTimeRangeErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1ComplianceReportsListCreatedByUsersErrorComponent
        | ApiV1ComplianceReportsListFrameworkRefsErrorComponent
        | ApiV1ComplianceReportsListKindErrorComponent
        | ApiV1ComplianceReportsListNameExactErrorComponent
        | ApiV1ComplianceReportsListOrganizationsErrorComponent
        | ApiV1ComplianceReportsListPeriodEndErrorComponent
        | ApiV1ComplianceReportsListPeriodEndGteErrorComponent
        | ApiV1ComplianceReportsListPeriodStartErrorComponent
        | ApiV1ComplianceReportsListPeriodStartLteErrorComponent
        | ApiV1ComplianceReportsListSearchErrorComponent
        | ApiV1ComplianceReportsListStateErrorComponent
        | ApiV1ComplianceReportsListStateNotErrorComponent
        | ApiV1ComplianceReportsListStatusErrorComponent
        | ApiV1ComplianceReportsListTimeRangeErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_compliance_reports_list_created_by_users_error_component import (
            ApiV1ComplianceReportsListCreatedByUsersErrorComponent,
        )
        from ..models.api_v1_compliance_reports_list_framework_refs_error_component import (
            ApiV1ComplianceReportsListFrameworkRefsErrorComponent,
        )
        from ..models.api_v1_compliance_reports_list_kind_error_component import (
            ApiV1ComplianceReportsListKindErrorComponent,
        )
        from ..models.api_v1_compliance_reports_list_organizations_error_component import (
            ApiV1ComplianceReportsListOrganizationsErrorComponent,
        )
        from ..models.api_v1_compliance_reports_list_period_end_error_component import (
            ApiV1ComplianceReportsListPeriodEndErrorComponent,
        )
        from ..models.api_v1_compliance_reports_list_period_end_gte_error_component import (
            ApiV1ComplianceReportsListPeriodEndGteErrorComponent,
        )
        from ..models.api_v1_compliance_reports_list_period_start_error_component import (
            ApiV1ComplianceReportsListPeriodStartErrorComponent,
        )
        from ..models.api_v1_compliance_reports_list_period_start_lte_error_component import (
            ApiV1ComplianceReportsListPeriodStartLteErrorComponent,
        )
        from ..models.api_v1_compliance_reports_list_search_error_component import (
            ApiV1ComplianceReportsListSearchErrorComponent,
        )
        from ..models.api_v1_compliance_reports_list_state_error_component import (
            ApiV1ComplianceReportsListStateErrorComponent,
        )
        from ..models.api_v1_compliance_reports_list_state_not_error_component import (
            ApiV1ComplianceReportsListStateNotErrorComponent,
        )
        from ..models.api_v1_compliance_reports_list_status_error_component import (
            ApiV1ComplianceReportsListStatusErrorComponent,
        )
        from ..models.api_v1_compliance_reports_list_time_range_error_component import (
            ApiV1ComplianceReportsListTimeRangeErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1ComplianceReportsListSearchErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ComplianceReportsListTimeRangeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ComplianceReportsListOrganizationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ComplianceReportsListStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ComplianceReportsListKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ComplianceReportsListCreatedByUsersErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ComplianceReportsListStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ComplianceReportsListPeriodStartErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ComplianceReportsListPeriodEndErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ComplianceReportsListPeriodStartLteErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ComplianceReportsListPeriodEndGteErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ComplianceReportsListFrameworkRefsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ComplianceReportsListStateNotErrorComponent):
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
        from ..models.api_v1_compliance_reports_list_created_by_users_error_component import (
            ApiV1ComplianceReportsListCreatedByUsersErrorComponent,
        )
        from ..models.api_v1_compliance_reports_list_framework_refs_error_component import (
            ApiV1ComplianceReportsListFrameworkRefsErrorComponent,
        )
        from ..models.api_v1_compliance_reports_list_kind_error_component import (
            ApiV1ComplianceReportsListKindErrorComponent,
        )
        from ..models.api_v1_compliance_reports_list_name_exact_error_component import (
            ApiV1ComplianceReportsListNameExactErrorComponent,
        )
        from ..models.api_v1_compliance_reports_list_organizations_error_component import (
            ApiV1ComplianceReportsListOrganizationsErrorComponent,
        )
        from ..models.api_v1_compliance_reports_list_period_end_error_component import (
            ApiV1ComplianceReportsListPeriodEndErrorComponent,
        )
        from ..models.api_v1_compliance_reports_list_period_end_gte_error_component import (
            ApiV1ComplianceReportsListPeriodEndGteErrorComponent,
        )
        from ..models.api_v1_compliance_reports_list_period_start_error_component import (
            ApiV1ComplianceReportsListPeriodStartErrorComponent,
        )
        from ..models.api_v1_compliance_reports_list_period_start_lte_error_component import (
            ApiV1ComplianceReportsListPeriodStartLteErrorComponent,
        )
        from ..models.api_v1_compliance_reports_list_search_error_component import (
            ApiV1ComplianceReportsListSearchErrorComponent,
        )
        from ..models.api_v1_compliance_reports_list_state_error_component import (
            ApiV1ComplianceReportsListStateErrorComponent,
        )
        from ..models.api_v1_compliance_reports_list_state_not_error_component import (
            ApiV1ComplianceReportsListStateNotErrorComponent,
        )
        from ..models.api_v1_compliance_reports_list_status_error_component import (
            ApiV1ComplianceReportsListStatusErrorComponent,
        )
        from ..models.api_v1_compliance_reports_list_time_range_error_component import (
            ApiV1ComplianceReportsListTimeRangeErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1ComplianceReportsListCreatedByUsersErrorComponent
                | ApiV1ComplianceReportsListFrameworkRefsErrorComponent
                | ApiV1ComplianceReportsListKindErrorComponent
                | ApiV1ComplianceReportsListNameExactErrorComponent
                | ApiV1ComplianceReportsListOrganizationsErrorComponent
                | ApiV1ComplianceReportsListPeriodEndErrorComponent
                | ApiV1ComplianceReportsListPeriodEndGteErrorComponent
                | ApiV1ComplianceReportsListPeriodStartErrorComponent
                | ApiV1ComplianceReportsListPeriodStartLteErrorComponent
                | ApiV1ComplianceReportsListSearchErrorComponent
                | ApiV1ComplianceReportsListStateErrorComponent
                | ApiV1ComplianceReportsListStateNotErrorComponent
                | ApiV1ComplianceReportsListStatusErrorComponent
                | ApiV1ComplianceReportsListTimeRangeErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_compliance_reports_list_error_type_0 = (
                        ApiV1ComplianceReportsListSearchErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_compliance_reports_list_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_compliance_reports_list_error_type_1 = (
                        ApiV1ComplianceReportsListTimeRangeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_compliance_reports_list_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_compliance_reports_list_error_type_2 = (
                        ApiV1ComplianceReportsListOrganizationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_compliance_reports_list_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_compliance_reports_list_error_type_3 = (
                        ApiV1ComplianceReportsListStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_compliance_reports_list_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_compliance_reports_list_error_type_4 = (
                        ApiV1ComplianceReportsListKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_compliance_reports_list_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_compliance_reports_list_error_type_5 = (
                        ApiV1ComplianceReportsListCreatedByUsersErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_compliance_reports_list_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_compliance_reports_list_error_type_6 = (
                        ApiV1ComplianceReportsListStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_compliance_reports_list_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_compliance_reports_list_error_type_7 = (
                        ApiV1ComplianceReportsListPeriodStartErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_compliance_reports_list_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_compliance_reports_list_error_type_8 = (
                        ApiV1ComplianceReportsListPeriodEndErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_compliance_reports_list_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_compliance_reports_list_error_type_9 = (
                        ApiV1ComplianceReportsListPeriodStartLteErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_compliance_reports_list_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_compliance_reports_list_error_type_10 = (
                        ApiV1ComplianceReportsListPeriodEndGteErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_compliance_reports_list_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_compliance_reports_list_error_type_11 = (
                        ApiV1ComplianceReportsListFrameworkRefsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_compliance_reports_list_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_compliance_reports_list_error_type_12 = (
                        ApiV1ComplianceReportsListStateNotErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_compliance_reports_list_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_compliance_reports_list_error_type_13 = (
                    ApiV1ComplianceReportsListNameExactErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_compliance_reports_list_error_type_13

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_compliance_reports_list_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_compliance_reports_list_validation_error.additional_properties = d
        return api_v1_compliance_reports_list_validation_error

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
