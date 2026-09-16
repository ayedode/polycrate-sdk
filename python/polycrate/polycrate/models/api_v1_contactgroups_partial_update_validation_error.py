from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_contactgroups_partial_update_dynamic_rules_error_component import (
        ApiV1ContactgroupsPartialUpdateDynamicRulesErrorComponent,
    )
    from ..models.api_v1_contactgroups_partial_update_email_error_component import (
        ApiV1ContactgroupsPartialUpdateEmailErrorComponent,
    )
    from ..models.api_v1_contactgroups_partial_update_keycloak_group_id_error_component import (
        ApiV1ContactgroupsPartialUpdateKeycloakGroupIdErrorComponent,
    )
    from ..models.api_v1_contactgroups_partial_update_kind_error_component import (
        ApiV1ContactgroupsPartialUpdateKindErrorComponent,
    )
    from ..models.api_v1_contactgroups_partial_update_name_error_component import (
        ApiV1ContactgroupsPartialUpdateNameErrorComponent,
    )
    from ..models.api_v1_contactgroups_partial_update_non_field_errors_error_component import (
        ApiV1ContactgroupsPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_contactgroups_partial_update_organization_id_error_component import (
        ApiV1ContactgroupsPartialUpdateOrganizationIdErrorComponent,
    )


T = TypeVar("T", bound="ApiV1ContactgroupsPartialUpdateValidationError")


@_attrs_define
class ApiV1ContactgroupsPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1ContactgroupsPartialUpdateDynamicRulesErrorComponent |
            ApiV1ContactgroupsPartialUpdateEmailErrorComponent |
            ApiV1ContactgroupsPartialUpdateKeycloakGroupIdErrorComponent | ApiV1ContactgroupsPartialUpdateKindErrorComponent
            | ApiV1ContactgroupsPartialUpdateNameErrorComponent |
            ApiV1ContactgroupsPartialUpdateNonFieldErrorsErrorComponent |
            ApiV1ContactgroupsPartialUpdateOrganizationIdErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1ContactgroupsPartialUpdateDynamicRulesErrorComponent
        | ApiV1ContactgroupsPartialUpdateEmailErrorComponent
        | ApiV1ContactgroupsPartialUpdateKeycloakGroupIdErrorComponent
        | ApiV1ContactgroupsPartialUpdateKindErrorComponent
        | ApiV1ContactgroupsPartialUpdateNameErrorComponent
        | ApiV1ContactgroupsPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1ContactgroupsPartialUpdateOrganizationIdErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_contactgroups_partial_update_dynamic_rules_error_component import (
            ApiV1ContactgroupsPartialUpdateDynamicRulesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_contactgroups_partial_update_email_error_component import (
            ApiV1ContactgroupsPartialUpdateEmailErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_contactgroups_partial_update_kind_error_component import (
            ApiV1ContactgroupsPartialUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_contactgroups_partial_update_name_error_component import (
            ApiV1ContactgroupsPartialUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_contactgroups_partial_update_non_field_errors_error_component import (
            ApiV1ContactgroupsPartialUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_contactgroups_partial_update_organization_id_error_component import (
            ApiV1ContactgroupsPartialUpdateOrganizationIdErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1ContactgroupsPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactgroupsPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactgroupsPartialUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactgroupsPartialUpdateOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactgroupsPartialUpdateEmailErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactgroupsPartialUpdateDynamicRulesErrorComponent):
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
        from ..models.api_v1_contactgroups_partial_update_dynamic_rules_error_component import (
            ApiV1ContactgroupsPartialUpdateDynamicRulesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_contactgroups_partial_update_email_error_component import (
            ApiV1ContactgroupsPartialUpdateEmailErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_contactgroups_partial_update_keycloak_group_id_error_component import (
            ApiV1ContactgroupsPartialUpdateKeycloakGroupIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_contactgroups_partial_update_kind_error_component import (
            ApiV1ContactgroupsPartialUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_contactgroups_partial_update_name_error_component import (
            ApiV1ContactgroupsPartialUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_contactgroups_partial_update_non_field_errors_error_component import (
            ApiV1ContactgroupsPartialUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_contactgroups_partial_update_organization_id_error_component import (
            ApiV1ContactgroupsPartialUpdateOrganizationIdErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1ContactgroupsPartialUpdateDynamicRulesErrorComponent
                | ApiV1ContactgroupsPartialUpdateEmailErrorComponent
                | ApiV1ContactgroupsPartialUpdateKeycloakGroupIdErrorComponent
                | ApiV1ContactgroupsPartialUpdateKindErrorComponent
                | ApiV1ContactgroupsPartialUpdateNameErrorComponent
                | ApiV1ContactgroupsPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1ContactgroupsPartialUpdateOrganizationIdErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contactgroups_partial_update_error_type_0 = (
                        ApiV1ContactgroupsPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contactgroups_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contactgroups_partial_update_error_type_1 = (
                        ApiV1ContactgroupsPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contactgroups_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contactgroups_partial_update_error_type_2 = (
                        ApiV1ContactgroupsPartialUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contactgroups_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contactgroups_partial_update_error_type_3 = (
                        ApiV1ContactgroupsPartialUpdateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contactgroups_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contactgroups_partial_update_error_type_4 = (
                        ApiV1ContactgroupsPartialUpdateEmailErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contactgroups_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contactgroups_partial_update_error_type_5 = (
                        ApiV1ContactgroupsPartialUpdateDynamicRulesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contactgroups_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_contactgroups_partial_update_error_type_6 = (
                    ApiV1ContactgroupsPartialUpdateKeycloakGroupIdErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_contactgroups_partial_update_error_type_6

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_contactgroups_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_contactgroups_partial_update_validation_error.additional_properties = d
        return api_v1_contactgroups_partial_update_validation_error

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
