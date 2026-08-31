from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_workspace_templates_update_description_error_component import (
        ApiV1WorkspaceTemplatesUpdateDescriptionErrorComponent,
    )
    from ..models.api_v1_workspace_templates_update_display_name_error_component import (
        ApiV1WorkspaceTemplatesUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_workspace_templates_update_is_default_error_component import (
        ApiV1WorkspaceTemplatesUpdateIsDefaultErrorComponent,
    )
    from ..models.api_v1_workspace_templates_update_name_error_component import (
        ApiV1WorkspaceTemplatesUpdateNameErrorComponent,
    )
    from ..models.api_v1_workspace_templates_update_non_field_errors_error_component import (
        ApiV1WorkspaceTemplatesUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_workspace_templates_update_organization_id_error_component import (
        ApiV1WorkspaceTemplatesUpdateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_workspace_templates_update_secrets_poly_template_error_component import (
        ApiV1WorkspaceTemplatesUpdateSecretsPolyTemplateErrorComponent,
    )
    from ..models.api_v1_workspace_templates_update_workspace_poly_template_error_component import (
        ApiV1WorkspaceTemplatesUpdateWorkspacePolyTemplateErrorComponent,
    )


T = TypeVar("T", bound="ApiV1WorkspaceTemplatesUpdateValidationError")


@_attrs_define
class ApiV1WorkspaceTemplatesUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1WorkspaceTemplatesUpdateDescriptionErrorComponent |
            ApiV1WorkspaceTemplatesUpdateDisplayNameErrorComponent | ApiV1WorkspaceTemplatesUpdateIsDefaultErrorComponent |
            ApiV1WorkspaceTemplatesUpdateNameErrorComponent | ApiV1WorkspaceTemplatesUpdateNonFieldErrorsErrorComponent |
            ApiV1WorkspaceTemplatesUpdateOrganizationIdErrorComponent |
            ApiV1WorkspaceTemplatesUpdateSecretsPolyTemplateErrorComponent |
            ApiV1WorkspaceTemplatesUpdateWorkspacePolyTemplateErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1WorkspaceTemplatesUpdateDescriptionErrorComponent
        | ApiV1WorkspaceTemplatesUpdateDisplayNameErrorComponent
        | ApiV1WorkspaceTemplatesUpdateIsDefaultErrorComponent
        | ApiV1WorkspaceTemplatesUpdateNameErrorComponent
        | ApiV1WorkspaceTemplatesUpdateNonFieldErrorsErrorComponent
        | ApiV1WorkspaceTemplatesUpdateOrganizationIdErrorComponent
        | ApiV1WorkspaceTemplatesUpdateSecretsPolyTemplateErrorComponent
        | ApiV1WorkspaceTemplatesUpdateWorkspacePolyTemplateErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_workspace_templates_update_description_error_component import (
            ApiV1WorkspaceTemplatesUpdateDescriptionErrorComponent,
        )
        from ..models.api_v1_workspace_templates_update_display_name_error_component import (
            ApiV1WorkspaceTemplatesUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_workspace_templates_update_name_error_component import (
            ApiV1WorkspaceTemplatesUpdateNameErrorComponent,
        )
        from ..models.api_v1_workspace_templates_update_non_field_errors_error_component import (
            ApiV1WorkspaceTemplatesUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_workspace_templates_update_organization_id_error_component import (
            ApiV1WorkspaceTemplatesUpdateOrganizationIdErrorComponent,
        )
        from ..models.api_v1_workspace_templates_update_secrets_poly_template_error_component import (
            ApiV1WorkspaceTemplatesUpdateSecretsPolyTemplateErrorComponent,
        )
        from ..models.api_v1_workspace_templates_update_workspace_poly_template_error_component import (
            ApiV1WorkspaceTemplatesUpdateWorkspacePolyTemplateErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1WorkspaceTemplatesUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspaceTemplatesUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspaceTemplatesUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspaceTemplatesUpdateOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspaceTemplatesUpdateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspaceTemplatesUpdateWorkspacePolyTemplateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspaceTemplatesUpdateSecretsPolyTemplateErrorComponent):
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
        from ..models.api_v1_workspace_templates_update_description_error_component import (
            ApiV1WorkspaceTemplatesUpdateDescriptionErrorComponent,
        )
        from ..models.api_v1_workspace_templates_update_display_name_error_component import (
            ApiV1WorkspaceTemplatesUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_workspace_templates_update_is_default_error_component import (
            ApiV1WorkspaceTemplatesUpdateIsDefaultErrorComponent,
        )
        from ..models.api_v1_workspace_templates_update_name_error_component import (
            ApiV1WorkspaceTemplatesUpdateNameErrorComponent,
        )
        from ..models.api_v1_workspace_templates_update_non_field_errors_error_component import (
            ApiV1WorkspaceTemplatesUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_workspace_templates_update_organization_id_error_component import (
            ApiV1WorkspaceTemplatesUpdateOrganizationIdErrorComponent,
        )
        from ..models.api_v1_workspace_templates_update_secrets_poly_template_error_component import (
            ApiV1WorkspaceTemplatesUpdateSecretsPolyTemplateErrorComponent,
        )
        from ..models.api_v1_workspace_templates_update_workspace_poly_template_error_component import (
            ApiV1WorkspaceTemplatesUpdateWorkspacePolyTemplateErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1WorkspaceTemplatesUpdateDescriptionErrorComponent
                | ApiV1WorkspaceTemplatesUpdateDisplayNameErrorComponent
                | ApiV1WorkspaceTemplatesUpdateIsDefaultErrorComponent
                | ApiV1WorkspaceTemplatesUpdateNameErrorComponent
                | ApiV1WorkspaceTemplatesUpdateNonFieldErrorsErrorComponent
                | ApiV1WorkspaceTemplatesUpdateOrganizationIdErrorComponent
                | ApiV1WorkspaceTemplatesUpdateSecretsPolyTemplateErrorComponent
                | ApiV1WorkspaceTemplatesUpdateWorkspacePolyTemplateErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspace_templates_update_error_type_0 = (
                        ApiV1WorkspaceTemplatesUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspace_templates_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspace_templates_update_error_type_1 = (
                        ApiV1WorkspaceTemplatesUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspace_templates_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspace_templates_update_error_type_2 = (
                        ApiV1WorkspaceTemplatesUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspace_templates_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspace_templates_update_error_type_3 = (
                        ApiV1WorkspaceTemplatesUpdateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspace_templates_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspace_templates_update_error_type_4 = (
                        ApiV1WorkspaceTemplatesUpdateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspace_templates_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspace_templates_update_error_type_5 = (
                        ApiV1WorkspaceTemplatesUpdateWorkspacePolyTemplateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspace_templates_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspace_templates_update_error_type_6 = (
                        ApiV1WorkspaceTemplatesUpdateSecretsPolyTemplateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspace_templates_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_workspace_templates_update_error_type_7 = (
                    ApiV1WorkspaceTemplatesUpdateIsDefaultErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_workspace_templates_update_error_type_7

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_workspace_templates_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_workspace_templates_update_validation_error.additional_properties = d
        return api_v1_workspace_templates_update_validation_error

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
