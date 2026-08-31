from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_workspace_templates_partial_update_description_error_component import (
        ApiV1WorkspaceTemplatesPartialUpdateDescriptionErrorComponent,
    )
    from ..models.api_v1_workspace_templates_partial_update_display_name_error_component import (
        ApiV1WorkspaceTemplatesPartialUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_workspace_templates_partial_update_is_default_error_component import (
        ApiV1WorkspaceTemplatesPartialUpdateIsDefaultErrorComponent,
    )
    from ..models.api_v1_workspace_templates_partial_update_name_error_component import (
        ApiV1WorkspaceTemplatesPartialUpdateNameErrorComponent,
    )
    from ..models.api_v1_workspace_templates_partial_update_non_field_errors_error_component import (
        ApiV1WorkspaceTemplatesPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_workspace_templates_partial_update_organization_id_error_component import (
        ApiV1WorkspaceTemplatesPartialUpdateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_workspace_templates_partial_update_secrets_poly_template_error_component import (
        ApiV1WorkspaceTemplatesPartialUpdateSecretsPolyTemplateErrorComponent,
    )
    from ..models.api_v1_workspace_templates_partial_update_workspace_poly_template_error_component import (
        ApiV1WorkspaceTemplatesPartialUpdateWorkspacePolyTemplateErrorComponent,
    )


T = TypeVar("T", bound="ApiV1WorkspaceTemplatesPartialUpdateValidationError")


@_attrs_define
class ApiV1WorkspaceTemplatesPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1WorkspaceTemplatesPartialUpdateDescriptionErrorComponent |
            ApiV1WorkspaceTemplatesPartialUpdateDisplayNameErrorComponent |
            ApiV1WorkspaceTemplatesPartialUpdateIsDefaultErrorComponent |
            ApiV1WorkspaceTemplatesPartialUpdateNameErrorComponent |
            ApiV1WorkspaceTemplatesPartialUpdateNonFieldErrorsErrorComponent |
            ApiV1WorkspaceTemplatesPartialUpdateOrganizationIdErrorComponent |
            ApiV1WorkspaceTemplatesPartialUpdateSecretsPolyTemplateErrorComponent |
            ApiV1WorkspaceTemplatesPartialUpdateWorkspacePolyTemplateErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1WorkspaceTemplatesPartialUpdateDescriptionErrorComponent
        | ApiV1WorkspaceTemplatesPartialUpdateDisplayNameErrorComponent
        | ApiV1WorkspaceTemplatesPartialUpdateIsDefaultErrorComponent
        | ApiV1WorkspaceTemplatesPartialUpdateNameErrorComponent
        | ApiV1WorkspaceTemplatesPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1WorkspaceTemplatesPartialUpdateOrganizationIdErrorComponent
        | ApiV1WorkspaceTemplatesPartialUpdateSecretsPolyTemplateErrorComponent
        | ApiV1WorkspaceTemplatesPartialUpdateWorkspacePolyTemplateErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_workspace_templates_partial_update_description_error_component import (
            ApiV1WorkspaceTemplatesPartialUpdateDescriptionErrorComponent,
        )
        from ..models.api_v1_workspace_templates_partial_update_display_name_error_component import (
            ApiV1WorkspaceTemplatesPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_workspace_templates_partial_update_name_error_component import (
            ApiV1WorkspaceTemplatesPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_workspace_templates_partial_update_non_field_errors_error_component import (
            ApiV1WorkspaceTemplatesPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_workspace_templates_partial_update_organization_id_error_component import (
            ApiV1WorkspaceTemplatesPartialUpdateOrganizationIdErrorComponent,
        )
        from ..models.api_v1_workspace_templates_partial_update_secrets_poly_template_error_component import (
            ApiV1WorkspaceTemplatesPartialUpdateSecretsPolyTemplateErrorComponent,
        )
        from ..models.api_v1_workspace_templates_partial_update_workspace_poly_template_error_component import (
            ApiV1WorkspaceTemplatesPartialUpdateWorkspacePolyTemplateErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1WorkspaceTemplatesPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspaceTemplatesPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspaceTemplatesPartialUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspaceTemplatesPartialUpdateOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspaceTemplatesPartialUpdateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspaceTemplatesPartialUpdateWorkspacePolyTemplateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspaceTemplatesPartialUpdateSecretsPolyTemplateErrorComponent):
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
        from ..models.api_v1_workspace_templates_partial_update_description_error_component import (
            ApiV1WorkspaceTemplatesPartialUpdateDescriptionErrorComponent,
        )
        from ..models.api_v1_workspace_templates_partial_update_display_name_error_component import (
            ApiV1WorkspaceTemplatesPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_workspace_templates_partial_update_is_default_error_component import (
            ApiV1WorkspaceTemplatesPartialUpdateIsDefaultErrorComponent,
        )
        from ..models.api_v1_workspace_templates_partial_update_name_error_component import (
            ApiV1WorkspaceTemplatesPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_workspace_templates_partial_update_non_field_errors_error_component import (
            ApiV1WorkspaceTemplatesPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_workspace_templates_partial_update_organization_id_error_component import (
            ApiV1WorkspaceTemplatesPartialUpdateOrganizationIdErrorComponent,
        )
        from ..models.api_v1_workspace_templates_partial_update_secrets_poly_template_error_component import (
            ApiV1WorkspaceTemplatesPartialUpdateSecretsPolyTemplateErrorComponent,
        )
        from ..models.api_v1_workspace_templates_partial_update_workspace_poly_template_error_component import (
            ApiV1WorkspaceTemplatesPartialUpdateWorkspacePolyTemplateErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1WorkspaceTemplatesPartialUpdateDescriptionErrorComponent
                | ApiV1WorkspaceTemplatesPartialUpdateDisplayNameErrorComponent
                | ApiV1WorkspaceTemplatesPartialUpdateIsDefaultErrorComponent
                | ApiV1WorkspaceTemplatesPartialUpdateNameErrorComponent
                | ApiV1WorkspaceTemplatesPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1WorkspaceTemplatesPartialUpdateOrganizationIdErrorComponent
                | ApiV1WorkspaceTemplatesPartialUpdateSecretsPolyTemplateErrorComponent
                | ApiV1WorkspaceTemplatesPartialUpdateWorkspacePolyTemplateErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspace_templates_partial_update_error_type_0 = (
                        ApiV1WorkspaceTemplatesPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspace_templates_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspace_templates_partial_update_error_type_1 = (
                        ApiV1WorkspaceTemplatesPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspace_templates_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspace_templates_partial_update_error_type_2 = (
                        ApiV1WorkspaceTemplatesPartialUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspace_templates_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspace_templates_partial_update_error_type_3 = (
                        ApiV1WorkspaceTemplatesPartialUpdateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspace_templates_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspace_templates_partial_update_error_type_4 = (
                        ApiV1WorkspaceTemplatesPartialUpdateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspace_templates_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspace_templates_partial_update_error_type_5 = (
                        ApiV1WorkspaceTemplatesPartialUpdateWorkspacePolyTemplateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspace_templates_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspace_templates_partial_update_error_type_6 = (
                        ApiV1WorkspaceTemplatesPartialUpdateSecretsPolyTemplateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspace_templates_partial_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_workspace_templates_partial_update_error_type_7 = (
                    ApiV1WorkspaceTemplatesPartialUpdateIsDefaultErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_workspace_templates_partial_update_error_type_7

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_workspace_templates_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_workspace_templates_partial_update_validation_error.additional_properties = d
        return api_v1_workspace_templates_partial_update_validation_error

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
