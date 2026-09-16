from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_domains_domain_registrars_list_created_at_error_component import (
        ApiV1DomainsDomainRegistrarsListCreatedAtErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_list_created_by_component_error_component import (
        ApiV1DomainsDomainRegistrarsListCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_list_created_by_users_error_component import (
        ApiV1DomainsDomainRegistrarsListCreatedByUsersErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_list_kind_error_component import (
        ApiV1DomainsDomainRegistrarsListKindErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_list_name_error_component import (
        ApiV1DomainsDomainRegistrarsListNameErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_list_name_exact_error_component import (
        ApiV1DomainsDomainRegistrarsListNameExactErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_list_organization_error_component import (
        ApiV1DomainsDomainRegistrarsListOrganizationErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_list_organizations_error_component import (
        ApiV1DomainsDomainRegistrarsListOrganizationsErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_list_scope_error_component import (
        ApiV1DomainsDomainRegistrarsListScopeErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_list_search_error_component import (
        ApiV1DomainsDomainRegistrarsListSearchErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_list_state_error_component import (
        ApiV1DomainsDomainRegistrarsListStateErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_list_state_not_error_component import (
        ApiV1DomainsDomainRegistrarsListStateNotErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_list_time_range_error_component import (
        ApiV1DomainsDomainRegistrarsListTimeRangeErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_list_updated_at_error_component import (
        ApiV1DomainsDomainRegistrarsListUpdatedAtErrorComponent,
    )


T = TypeVar("T", bound="ApiV1DomainsDomainRegistrarsListValidationError")


@_attrs_define
class ApiV1DomainsDomainRegistrarsListValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1DomainsDomainRegistrarsListCreatedAtErrorComponent |
            ApiV1DomainsDomainRegistrarsListCreatedByComponentErrorComponent |
            ApiV1DomainsDomainRegistrarsListCreatedByUsersErrorComponent |
            ApiV1DomainsDomainRegistrarsListKindErrorComponent | ApiV1DomainsDomainRegistrarsListNameErrorComponent |
            ApiV1DomainsDomainRegistrarsListNameExactErrorComponent |
            ApiV1DomainsDomainRegistrarsListOrganizationErrorComponent |
            ApiV1DomainsDomainRegistrarsListOrganizationsErrorComponent |
            ApiV1DomainsDomainRegistrarsListScopeErrorComponent | ApiV1DomainsDomainRegistrarsListSearchErrorComponent |
            ApiV1DomainsDomainRegistrarsListStateErrorComponent | ApiV1DomainsDomainRegistrarsListStateNotErrorComponent |
            ApiV1DomainsDomainRegistrarsListTimeRangeErrorComponent |
            ApiV1DomainsDomainRegistrarsListUpdatedAtErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1DomainsDomainRegistrarsListCreatedAtErrorComponent
        | ApiV1DomainsDomainRegistrarsListCreatedByComponentErrorComponent
        | ApiV1DomainsDomainRegistrarsListCreatedByUsersErrorComponent
        | ApiV1DomainsDomainRegistrarsListKindErrorComponent
        | ApiV1DomainsDomainRegistrarsListNameErrorComponent
        | ApiV1DomainsDomainRegistrarsListNameExactErrorComponent
        | ApiV1DomainsDomainRegistrarsListOrganizationErrorComponent
        | ApiV1DomainsDomainRegistrarsListOrganizationsErrorComponent
        | ApiV1DomainsDomainRegistrarsListScopeErrorComponent
        | ApiV1DomainsDomainRegistrarsListSearchErrorComponent
        | ApiV1DomainsDomainRegistrarsListStateErrorComponent
        | ApiV1DomainsDomainRegistrarsListStateNotErrorComponent
        | ApiV1DomainsDomainRegistrarsListTimeRangeErrorComponent
        | ApiV1DomainsDomainRegistrarsListUpdatedAtErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_domains_domain_registrars_list_created_at_error_component import (
            ApiV1DomainsDomainRegistrarsListCreatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_list_created_by_component_error_component import (
            ApiV1DomainsDomainRegistrarsListCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_list_created_by_users_error_component import (
            ApiV1DomainsDomainRegistrarsListCreatedByUsersErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_list_kind_error_component import (
            ApiV1DomainsDomainRegistrarsListKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_list_name_error_component import (
            ApiV1DomainsDomainRegistrarsListNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_list_organization_error_component import (
            ApiV1DomainsDomainRegistrarsListOrganizationErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_list_organizations_error_component import (
            ApiV1DomainsDomainRegistrarsListOrganizationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_list_scope_error_component import (
            ApiV1DomainsDomainRegistrarsListScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_list_search_error_component import (
            ApiV1DomainsDomainRegistrarsListSearchErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_list_state_error_component import (
            ApiV1DomainsDomainRegistrarsListStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_list_state_not_error_component import (
            ApiV1DomainsDomainRegistrarsListStateNotErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_list_time_range_error_component import (
            ApiV1DomainsDomainRegistrarsListTimeRangeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_list_updated_at_error_component import (
            ApiV1DomainsDomainRegistrarsListUpdatedAtErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsListSearchErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsListTimeRangeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsListOrganizationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsListStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsListKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsListCreatedByUsersErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsListCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsListNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsListCreatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsListUpdatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsListScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsListOrganizationErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsListStateNotErrorComponent):
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
        from ..models.api_v1_domains_domain_registrars_list_created_at_error_component import (
            ApiV1DomainsDomainRegistrarsListCreatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_list_created_by_component_error_component import (
            ApiV1DomainsDomainRegistrarsListCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_list_created_by_users_error_component import (
            ApiV1DomainsDomainRegistrarsListCreatedByUsersErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_list_kind_error_component import (
            ApiV1DomainsDomainRegistrarsListKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_list_name_error_component import (
            ApiV1DomainsDomainRegistrarsListNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_list_name_exact_error_component import (
            ApiV1DomainsDomainRegistrarsListNameExactErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_list_organization_error_component import (
            ApiV1DomainsDomainRegistrarsListOrganizationErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_list_organizations_error_component import (
            ApiV1DomainsDomainRegistrarsListOrganizationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_list_scope_error_component import (
            ApiV1DomainsDomainRegistrarsListScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_list_search_error_component import (
            ApiV1DomainsDomainRegistrarsListSearchErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_list_state_error_component import (
            ApiV1DomainsDomainRegistrarsListStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_list_state_not_error_component import (
            ApiV1DomainsDomainRegistrarsListStateNotErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_list_time_range_error_component import (
            ApiV1DomainsDomainRegistrarsListTimeRangeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_list_updated_at_error_component import (
            ApiV1DomainsDomainRegistrarsListUpdatedAtErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1DomainsDomainRegistrarsListCreatedAtErrorComponent
                | ApiV1DomainsDomainRegistrarsListCreatedByComponentErrorComponent
                | ApiV1DomainsDomainRegistrarsListCreatedByUsersErrorComponent
                | ApiV1DomainsDomainRegistrarsListKindErrorComponent
                | ApiV1DomainsDomainRegistrarsListNameErrorComponent
                | ApiV1DomainsDomainRegistrarsListNameExactErrorComponent
                | ApiV1DomainsDomainRegistrarsListOrganizationErrorComponent
                | ApiV1DomainsDomainRegistrarsListOrganizationsErrorComponent
                | ApiV1DomainsDomainRegistrarsListScopeErrorComponent
                | ApiV1DomainsDomainRegistrarsListSearchErrorComponent
                | ApiV1DomainsDomainRegistrarsListStateErrorComponent
                | ApiV1DomainsDomainRegistrarsListStateNotErrorComponent
                | ApiV1DomainsDomainRegistrarsListTimeRangeErrorComponent
                | ApiV1DomainsDomainRegistrarsListUpdatedAtErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_list_error_type_0 = (
                        ApiV1DomainsDomainRegistrarsListSearchErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_list_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_list_error_type_1 = (
                        ApiV1DomainsDomainRegistrarsListTimeRangeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_list_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_list_error_type_2 = (
                        ApiV1DomainsDomainRegistrarsListOrganizationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_list_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_list_error_type_3 = (
                        ApiV1DomainsDomainRegistrarsListStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_list_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_list_error_type_4 = (
                        ApiV1DomainsDomainRegistrarsListKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_list_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_list_error_type_5 = (
                        ApiV1DomainsDomainRegistrarsListCreatedByUsersErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_list_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_list_error_type_6 = (
                        ApiV1DomainsDomainRegistrarsListCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_list_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_list_error_type_7 = (
                        ApiV1DomainsDomainRegistrarsListNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_list_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_list_error_type_8 = (
                        ApiV1DomainsDomainRegistrarsListCreatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_list_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_list_error_type_9 = (
                        ApiV1DomainsDomainRegistrarsListUpdatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_list_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_list_error_type_10 = (
                        ApiV1DomainsDomainRegistrarsListScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_list_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_list_error_type_11 = (
                        ApiV1DomainsDomainRegistrarsListOrganizationErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_list_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_list_error_type_12 = (
                        ApiV1DomainsDomainRegistrarsListStateNotErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_list_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_domains_domain_registrars_list_error_type_13 = (
                    ApiV1DomainsDomainRegistrarsListNameExactErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_domains_domain_registrars_list_error_type_13

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_domains_domain_registrars_list_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_domains_domain_registrars_list_validation_error.additional_properties = d
        return api_v1_domains_domain_registrars_list_validation_error

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
