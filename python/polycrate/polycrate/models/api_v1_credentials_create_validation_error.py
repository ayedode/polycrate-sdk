from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_credentials_create_api_endpoint_error_component import (
        ApiV1CredentialsCreateApiEndpointErrorComponent,
    )
    from ..models.api_v1_credentials_create_api_key_error_component import ApiV1CredentialsCreateApiKeyErrorComponent
    from ..models.api_v1_credentials_create_api_user_error_component import ApiV1CredentialsCreateApiUserErrorComponent
    from ..models.api_v1_credentials_create_description_error_component import (
        ApiV1CredentialsCreateDescriptionErrorComponent,
    )
    from ..models.api_v1_credentials_create_kind_error_component import ApiV1CredentialsCreateKindErrorComponent
    from ..models.api_v1_credentials_create_kubeconfig_error_component import (
        ApiV1CredentialsCreateKubeconfigErrorComponent,
    )
    from ..models.api_v1_credentials_create_metadata_error_component import ApiV1CredentialsCreateMetadataErrorComponent
    from ..models.api_v1_credentials_create_name_error_component import ApiV1CredentialsCreateNameErrorComponent
    from ..models.api_v1_credentials_create_non_field_errors_error_component import (
        ApiV1CredentialsCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_credentials_create_organization_error_component import (
        ApiV1CredentialsCreateOrganizationErrorComponent,
    )
    from ..models.api_v1_credentials_create_ssh_private_key_error_component import (
        ApiV1CredentialsCreateSshPrivateKeyErrorComponent,
    )
    from ..models.api_v1_credentials_create_ssh_public_key_error_component import (
        ApiV1CredentialsCreateSshPublicKeyErrorComponent,
    )
    from ..models.api_v1_credentials_create_workspace_error_component import (
        ApiV1CredentialsCreateWorkspaceErrorComponent,
    )


T = TypeVar("T", bound="ApiV1CredentialsCreateValidationError")


@_attrs_define
class ApiV1CredentialsCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1CredentialsCreateApiEndpointErrorComponent | ApiV1CredentialsCreateApiKeyErrorComponent |
            ApiV1CredentialsCreateApiUserErrorComponent | ApiV1CredentialsCreateDescriptionErrorComponent |
            ApiV1CredentialsCreateKindErrorComponent | ApiV1CredentialsCreateKubeconfigErrorComponent |
            ApiV1CredentialsCreateMetadataErrorComponent | ApiV1CredentialsCreateNameErrorComponent |
            ApiV1CredentialsCreateNonFieldErrorsErrorComponent | ApiV1CredentialsCreateOrganizationErrorComponent |
            ApiV1CredentialsCreateSshPrivateKeyErrorComponent | ApiV1CredentialsCreateSshPublicKeyErrorComponent |
            ApiV1CredentialsCreateWorkspaceErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1CredentialsCreateApiEndpointErrorComponent
        | ApiV1CredentialsCreateApiKeyErrorComponent
        | ApiV1CredentialsCreateApiUserErrorComponent
        | ApiV1CredentialsCreateDescriptionErrorComponent
        | ApiV1CredentialsCreateKindErrorComponent
        | ApiV1CredentialsCreateKubeconfigErrorComponent
        | ApiV1CredentialsCreateMetadataErrorComponent
        | ApiV1CredentialsCreateNameErrorComponent
        | ApiV1CredentialsCreateNonFieldErrorsErrorComponent
        | ApiV1CredentialsCreateOrganizationErrorComponent
        | ApiV1CredentialsCreateSshPrivateKeyErrorComponent
        | ApiV1CredentialsCreateSshPublicKeyErrorComponent
        | ApiV1CredentialsCreateWorkspaceErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_credentials_create_api_endpoint_error_component import (
            ApiV1CredentialsCreateApiEndpointErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_create_api_key_error_component import (
            ApiV1CredentialsCreateApiKeyErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_create_api_user_error_component import (
            ApiV1CredentialsCreateApiUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_create_description_error_component import (
            ApiV1CredentialsCreateDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_create_kind_error_component import (
            ApiV1CredentialsCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_create_kubeconfig_error_component import (
            ApiV1CredentialsCreateKubeconfigErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_create_name_error_component import (
            ApiV1CredentialsCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_create_non_field_errors_error_component import (
            ApiV1CredentialsCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_create_organization_error_component import (
            ApiV1CredentialsCreateOrganizationErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_create_ssh_private_key_error_component import (
            ApiV1CredentialsCreateSshPrivateKeyErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_create_ssh_public_key_error_component import (
            ApiV1CredentialsCreateSshPublicKeyErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_create_workspace_error_component import (
            ApiV1CredentialsCreateWorkspaceErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1CredentialsCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsCreateOrganizationErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsCreateWorkspaceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsCreateApiEndpointErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsCreateApiUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsCreateApiKeyErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsCreateKubeconfigErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsCreateSshPrivateKeyErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsCreateSshPublicKeyErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsCreateDescriptionErrorComponent):
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
        from ..models.api_v1_credentials_create_api_endpoint_error_component import (
            ApiV1CredentialsCreateApiEndpointErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_create_api_key_error_component import (
            ApiV1CredentialsCreateApiKeyErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_create_api_user_error_component import (
            ApiV1CredentialsCreateApiUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_create_description_error_component import (
            ApiV1CredentialsCreateDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_create_kind_error_component import (
            ApiV1CredentialsCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_create_kubeconfig_error_component import (
            ApiV1CredentialsCreateKubeconfigErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_create_metadata_error_component import (
            ApiV1CredentialsCreateMetadataErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_create_name_error_component import (
            ApiV1CredentialsCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_create_non_field_errors_error_component import (
            ApiV1CredentialsCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_create_organization_error_component import (
            ApiV1CredentialsCreateOrganizationErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_create_ssh_private_key_error_component import (
            ApiV1CredentialsCreateSshPrivateKeyErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_create_ssh_public_key_error_component import (
            ApiV1CredentialsCreateSshPublicKeyErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_create_workspace_error_component import (
            ApiV1CredentialsCreateWorkspaceErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1CredentialsCreateApiEndpointErrorComponent
                | ApiV1CredentialsCreateApiKeyErrorComponent
                | ApiV1CredentialsCreateApiUserErrorComponent
                | ApiV1CredentialsCreateDescriptionErrorComponent
                | ApiV1CredentialsCreateKindErrorComponent
                | ApiV1CredentialsCreateKubeconfigErrorComponent
                | ApiV1CredentialsCreateMetadataErrorComponent
                | ApiV1CredentialsCreateNameErrorComponent
                | ApiV1CredentialsCreateNonFieldErrorsErrorComponent
                | ApiV1CredentialsCreateOrganizationErrorComponent
                | ApiV1CredentialsCreateSshPrivateKeyErrorComponent
                | ApiV1CredentialsCreateSshPublicKeyErrorComponent
                | ApiV1CredentialsCreateWorkspaceErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_create_error_type_0 = (
                        ApiV1CredentialsCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_create_error_type_1 = (
                        ApiV1CredentialsCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_create_error_type_2 = (
                        ApiV1CredentialsCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_create_error_type_3 = (
                        ApiV1CredentialsCreateOrganizationErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_create_error_type_4 = (
                        ApiV1CredentialsCreateWorkspaceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_create_error_type_5 = (
                        ApiV1CredentialsCreateApiEndpointErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_create_error_type_6 = (
                        ApiV1CredentialsCreateApiUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_create_error_type_7 = (
                        ApiV1CredentialsCreateApiKeyErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_create_error_type_8 = (
                        ApiV1CredentialsCreateKubeconfigErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_create_error_type_9 = (
                        ApiV1CredentialsCreateSshPrivateKeyErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_create_error_type_10 = (
                        ApiV1CredentialsCreateSshPublicKeyErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_create_error_type_11 = (
                        ApiV1CredentialsCreateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_credentials_create_error_type_12 = (
                    ApiV1CredentialsCreateMetadataErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_credentials_create_error_type_12

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_credentials_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_credentials_create_validation_error.additional_properties = d
        return api_v1_credentials_create_validation_error

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
