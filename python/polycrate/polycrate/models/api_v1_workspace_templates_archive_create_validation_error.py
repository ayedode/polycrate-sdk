from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_workspace_templates_archive_create_description_error_component import (
        ApiV1WorkspaceTemplatesArchiveCreateDescriptionErrorComponent,
    )
    from ..models.api_v1_workspace_templates_archive_create_display_name_error_component import (
        ApiV1WorkspaceTemplatesArchiveCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_workspace_templates_archive_create_is_default_error_component import (
        ApiV1WorkspaceTemplatesArchiveCreateIsDefaultErrorComponent,
    )
    from ..models.api_v1_workspace_templates_archive_create_name_error_component import (
        ApiV1WorkspaceTemplatesArchiveCreateNameErrorComponent,
    )
    from ..models.api_v1_workspace_templates_archive_create_non_field_errors_error_component import (
        ApiV1WorkspaceTemplatesArchiveCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_workspace_templates_archive_create_organization_id_error_component import (
        ApiV1WorkspaceTemplatesArchiveCreateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_workspace_templates_archive_create_secrets_poly_template_error_component import (
        ApiV1WorkspaceTemplatesArchiveCreateSecretsPolyTemplateErrorComponent,
    )
    from ..models.api_v1_workspace_templates_archive_create_workspace_poly_template_error_component import (
        ApiV1WorkspaceTemplatesArchiveCreateWorkspacePolyTemplateErrorComponent,
    )


T = TypeVar("T", bound="ApiV1WorkspaceTemplatesArchiveCreateValidationError")


@_attrs_define
class ApiV1WorkspaceTemplatesArchiveCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1WorkspaceTemplatesArchiveCreateDescriptionErrorComponent |
            ApiV1WorkspaceTemplatesArchiveCreateDisplayNameErrorComponent |
            ApiV1WorkspaceTemplatesArchiveCreateIsDefaultErrorComponent |
            ApiV1WorkspaceTemplatesArchiveCreateNameErrorComponent |
            ApiV1WorkspaceTemplatesArchiveCreateNonFieldErrorsErrorComponent |
            ApiV1WorkspaceTemplatesArchiveCreateOrganizationIdErrorComponent |
            ApiV1WorkspaceTemplatesArchiveCreateSecretsPolyTemplateErrorComponent |
            ApiV1WorkspaceTemplatesArchiveCreateWorkspacePolyTemplateErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1WorkspaceTemplatesArchiveCreateDescriptionErrorComponent
        | ApiV1WorkspaceTemplatesArchiveCreateDisplayNameErrorComponent
        | ApiV1WorkspaceTemplatesArchiveCreateIsDefaultErrorComponent
        | ApiV1WorkspaceTemplatesArchiveCreateNameErrorComponent
        | ApiV1WorkspaceTemplatesArchiveCreateNonFieldErrorsErrorComponent
        | ApiV1WorkspaceTemplatesArchiveCreateOrganizationIdErrorComponent
        | ApiV1WorkspaceTemplatesArchiveCreateSecretsPolyTemplateErrorComponent
        | ApiV1WorkspaceTemplatesArchiveCreateWorkspacePolyTemplateErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_workspace_templates_archive_create_description_error_component import (
            ApiV1WorkspaceTemplatesArchiveCreateDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspace_templates_archive_create_display_name_error_component import (
            ApiV1WorkspaceTemplatesArchiveCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspace_templates_archive_create_name_error_component import (
            ApiV1WorkspaceTemplatesArchiveCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspace_templates_archive_create_non_field_errors_error_component import (
            ApiV1WorkspaceTemplatesArchiveCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspace_templates_archive_create_organization_id_error_component import (
            ApiV1WorkspaceTemplatesArchiveCreateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspace_templates_archive_create_secrets_poly_template_error_component import (
            ApiV1WorkspaceTemplatesArchiveCreateSecretsPolyTemplateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspace_templates_archive_create_workspace_poly_template_error_component import (
            ApiV1WorkspaceTemplatesArchiveCreateWorkspacePolyTemplateErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1WorkspaceTemplatesArchiveCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspaceTemplatesArchiveCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspaceTemplatesArchiveCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspaceTemplatesArchiveCreateOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspaceTemplatesArchiveCreateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspaceTemplatesArchiveCreateWorkspacePolyTemplateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspaceTemplatesArchiveCreateSecretsPolyTemplateErrorComponent):
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
        from ..models.api_v1_workspace_templates_archive_create_description_error_component import (
            ApiV1WorkspaceTemplatesArchiveCreateDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspace_templates_archive_create_display_name_error_component import (
            ApiV1WorkspaceTemplatesArchiveCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspace_templates_archive_create_is_default_error_component import (
            ApiV1WorkspaceTemplatesArchiveCreateIsDefaultErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspace_templates_archive_create_name_error_component import (
            ApiV1WorkspaceTemplatesArchiveCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspace_templates_archive_create_non_field_errors_error_component import (
            ApiV1WorkspaceTemplatesArchiveCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspace_templates_archive_create_organization_id_error_component import (
            ApiV1WorkspaceTemplatesArchiveCreateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspace_templates_archive_create_secrets_poly_template_error_component import (
            ApiV1WorkspaceTemplatesArchiveCreateSecretsPolyTemplateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_workspace_templates_archive_create_workspace_poly_template_error_component import (
            ApiV1WorkspaceTemplatesArchiveCreateWorkspacePolyTemplateErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1WorkspaceTemplatesArchiveCreateDescriptionErrorComponent
                | ApiV1WorkspaceTemplatesArchiveCreateDisplayNameErrorComponent
                | ApiV1WorkspaceTemplatesArchiveCreateIsDefaultErrorComponent
                | ApiV1WorkspaceTemplatesArchiveCreateNameErrorComponent
                | ApiV1WorkspaceTemplatesArchiveCreateNonFieldErrorsErrorComponent
                | ApiV1WorkspaceTemplatesArchiveCreateOrganizationIdErrorComponent
                | ApiV1WorkspaceTemplatesArchiveCreateSecretsPolyTemplateErrorComponent
                | ApiV1WorkspaceTemplatesArchiveCreateWorkspacePolyTemplateErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspace_templates_archive_create_error_type_0 = (
                        ApiV1WorkspaceTemplatesArchiveCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspace_templates_archive_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspace_templates_archive_create_error_type_1 = (
                        ApiV1WorkspaceTemplatesArchiveCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspace_templates_archive_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspace_templates_archive_create_error_type_2 = (
                        ApiV1WorkspaceTemplatesArchiveCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspace_templates_archive_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspace_templates_archive_create_error_type_3 = (
                        ApiV1WorkspaceTemplatesArchiveCreateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspace_templates_archive_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspace_templates_archive_create_error_type_4 = (
                        ApiV1WorkspaceTemplatesArchiveCreateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspace_templates_archive_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspace_templates_archive_create_error_type_5 = (
                        ApiV1WorkspaceTemplatesArchiveCreateWorkspacePolyTemplateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspace_templates_archive_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspace_templates_archive_create_error_type_6 = (
                        ApiV1WorkspaceTemplatesArchiveCreateSecretsPolyTemplateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspace_templates_archive_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_workspace_templates_archive_create_error_type_7 = (
                    ApiV1WorkspaceTemplatesArchiveCreateIsDefaultErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_workspace_templates_archive_create_error_type_7

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_workspace_templates_archive_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_workspace_templates_archive_create_validation_error.additional_properties = d
        return api_v1_workspace_templates_archive_create_validation_error

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
