from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_credentials_archive_create_annotations_error_component import (
        ApiV1CredentialsArchiveCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_credentials_archive_create_api_endpoint_error_component import (
        ApiV1CredentialsArchiveCreateApiEndpointErrorComponent,
    )
    from ..models.api_v1_credentials_archive_create_api_key_error_component import (
        ApiV1CredentialsArchiveCreateApiKeyErrorComponent,
    )
    from ..models.api_v1_credentials_archive_create_api_user_error_component import (
        ApiV1CredentialsArchiveCreateApiUserErrorComponent,
    )
    from ..models.api_v1_credentials_archive_create_archived_at_error_component import (
        ApiV1CredentialsArchiveCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_credentials_archive_create_archived_error_component import (
        ApiV1CredentialsArchiveCreateArchivedErrorComponent,
    )
    from ..models.api_v1_credentials_archive_create_archived_reason_error_component import (
        ApiV1CredentialsArchiveCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_credentials_archive_create_criticality_error_component import (
        ApiV1CredentialsArchiveCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_credentials_archive_create_debug_mode_error_component import (
        ApiV1CredentialsArchiveCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_credentials_archive_create_description_error_component import (
        ApiV1CredentialsArchiveCreateDescriptionErrorComponent,
    )
    from ..models.api_v1_credentials_archive_create_display_name_error_component import (
        ApiV1CredentialsArchiveCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_credentials_archive_create_kind_error_component import (
        ApiV1CredentialsArchiveCreateKindErrorComponent,
    )
    from ..models.api_v1_credentials_archive_create_kubeconfig_error_component import (
        ApiV1CredentialsArchiveCreateKubeconfigErrorComponent,
    )
    from ..models.api_v1_credentials_archive_create_labels_error_component import (
        ApiV1CredentialsArchiveCreateLabelsErrorComponent,
    )
    from ..models.api_v1_credentials_archive_create_metadata_error_component import (
        ApiV1CredentialsArchiveCreateMetadataErrorComponent,
    )
    from ..models.api_v1_credentials_archive_create_name_error_component import (
        ApiV1CredentialsArchiveCreateNameErrorComponent,
    )
    from ..models.api_v1_credentials_archive_create_non_field_errors_error_component import (
        ApiV1CredentialsArchiveCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_credentials_archive_create_platform_service_error_component import (
        ApiV1CredentialsArchiveCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_credentials_archive_create_provider_error_component import (
        ApiV1CredentialsArchiveCreateProviderErrorComponent,
    )
    from ..models.api_v1_credentials_archive_create_provider_id_error_component import (
        ApiV1CredentialsArchiveCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_credentials_archive_create_provider_reference_error_component import (
        ApiV1CredentialsArchiveCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_credentials_archive_create_reconciliation_enabled_error_component import (
        ApiV1CredentialsArchiveCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_credentials_archive_create_sla_availability_error_component import (
        ApiV1CredentialsArchiveCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_credentials_archive_create_sla_target_error_component import (
        ApiV1CredentialsArchiveCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_credentials_archive_create_slo_availability_error_component import (
        ApiV1CredentialsArchiveCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_credentials_archive_create_slo_target_error_component import (
        ApiV1CredentialsArchiveCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_credentials_archive_create_ssh_private_key_error_component import (
        ApiV1CredentialsArchiveCreateSshPrivateKeyErrorComponent,
    )
    from ..models.api_v1_credentials_archive_create_ssh_public_key_error_component import (
        ApiV1CredentialsArchiveCreateSshPublicKeyErrorComponent,
    )
    from ..models.api_v1_credentials_archive_create_target_availability_error_component import (
        ApiV1CredentialsArchiveCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_credentials_archive_create_tolerations_error_component import (
        ApiV1CredentialsArchiveCreateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1CredentialsArchiveCreateValidationError")


@_attrs_define
class ApiV1CredentialsArchiveCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1CredentialsArchiveCreateAnnotationsErrorComponent |
            ApiV1CredentialsArchiveCreateApiEndpointErrorComponent | ApiV1CredentialsArchiveCreateApiKeyErrorComponent |
            ApiV1CredentialsArchiveCreateApiUserErrorComponent | ApiV1CredentialsArchiveCreateArchivedAtErrorComponent |
            ApiV1CredentialsArchiveCreateArchivedErrorComponent | ApiV1CredentialsArchiveCreateArchivedReasonErrorComponent
            | ApiV1CredentialsArchiveCreateCriticalityErrorComponent | ApiV1CredentialsArchiveCreateDebugModeErrorComponent
            | ApiV1CredentialsArchiveCreateDescriptionErrorComponent |
            ApiV1CredentialsArchiveCreateDisplayNameErrorComponent | ApiV1CredentialsArchiveCreateKindErrorComponent |
            ApiV1CredentialsArchiveCreateKubeconfigErrorComponent | ApiV1CredentialsArchiveCreateLabelsErrorComponent |
            ApiV1CredentialsArchiveCreateMetadataErrorComponent | ApiV1CredentialsArchiveCreateNameErrorComponent |
            ApiV1CredentialsArchiveCreateNonFieldErrorsErrorComponent |
            ApiV1CredentialsArchiveCreatePlatformServiceErrorComponent | ApiV1CredentialsArchiveCreateProviderErrorComponent
            | ApiV1CredentialsArchiveCreateProviderIdErrorComponent |
            ApiV1CredentialsArchiveCreateProviderReferenceErrorComponent |
            ApiV1CredentialsArchiveCreateReconciliationEnabledErrorComponent |
            ApiV1CredentialsArchiveCreateSlaAvailabilityErrorComponent |
            ApiV1CredentialsArchiveCreateSlaTargetErrorComponent |
            ApiV1CredentialsArchiveCreateSloAvailabilityErrorComponent |
            ApiV1CredentialsArchiveCreateSloTargetErrorComponent | ApiV1CredentialsArchiveCreateSshPrivateKeyErrorComponent
            | ApiV1CredentialsArchiveCreateSshPublicKeyErrorComponent |
            ApiV1CredentialsArchiveCreateTargetAvailabilityErrorComponent |
            ApiV1CredentialsArchiveCreateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1CredentialsArchiveCreateAnnotationsErrorComponent
        | ApiV1CredentialsArchiveCreateApiEndpointErrorComponent
        | ApiV1CredentialsArchiveCreateApiKeyErrorComponent
        | ApiV1CredentialsArchiveCreateApiUserErrorComponent
        | ApiV1CredentialsArchiveCreateArchivedAtErrorComponent
        | ApiV1CredentialsArchiveCreateArchivedErrorComponent
        | ApiV1CredentialsArchiveCreateArchivedReasonErrorComponent
        | ApiV1CredentialsArchiveCreateCriticalityErrorComponent
        | ApiV1CredentialsArchiveCreateDebugModeErrorComponent
        | ApiV1CredentialsArchiveCreateDescriptionErrorComponent
        | ApiV1CredentialsArchiveCreateDisplayNameErrorComponent
        | ApiV1CredentialsArchiveCreateKindErrorComponent
        | ApiV1CredentialsArchiveCreateKubeconfigErrorComponent
        | ApiV1CredentialsArchiveCreateLabelsErrorComponent
        | ApiV1CredentialsArchiveCreateMetadataErrorComponent
        | ApiV1CredentialsArchiveCreateNameErrorComponent
        | ApiV1CredentialsArchiveCreateNonFieldErrorsErrorComponent
        | ApiV1CredentialsArchiveCreatePlatformServiceErrorComponent
        | ApiV1CredentialsArchiveCreateProviderErrorComponent
        | ApiV1CredentialsArchiveCreateProviderIdErrorComponent
        | ApiV1CredentialsArchiveCreateProviderReferenceErrorComponent
        | ApiV1CredentialsArchiveCreateReconciliationEnabledErrorComponent
        | ApiV1CredentialsArchiveCreateSlaAvailabilityErrorComponent
        | ApiV1CredentialsArchiveCreateSlaTargetErrorComponent
        | ApiV1CredentialsArchiveCreateSloAvailabilityErrorComponent
        | ApiV1CredentialsArchiveCreateSloTargetErrorComponent
        | ApiV1CredentialsArchiveCreateSshPrivateKeyErrorComponent
        | ApiV1CredentialsArchiveCreateSshPublicKeyErrorComponent
        | ApiV1CredentialsArchiveCreateTargetAvailabilityErrorComponent
        | ApiV1CredentialsArchiveCreateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_credentials_archive_create_annotations_error_component import (
            ApiV1CredentialsArchiveCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_credentials_archive_create_api_endpoint_error_component import (
            ApiV1CredentialsArchiveCreateApiEndpointErrorComponent,
        )
        from ..models.api_v1_credentials_archive_create_api_key_error_component import (
            ApiV1CredentialsArchiveCreateApiKeyErrorComponent,
        )
        from ..models.api_v1_credentials_archive_create_api_user_error_component import (
            ApiV1CredentialsArchiveCreateApiUserErrorComponent,
        )
        from ..models.api_v1_credentials_archive_create_archived_at_error_component import (
            ApiV1CredentialsArchiveCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_credentials_archive_create_archived_error_component import (
            ApiV1CredentialsArchiveCreateArchivedErrorComponent,
        )
        from ..models.api_v1_credentials_archive_create_archived_reason_error_component import (
            ApiV1CredentialsArchiveCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_credentials_archive_create_criticality_error_component import (
            ApiV1CredentialsArchiveCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_credentials_archive_create_debug_mode_error_component import (
            ApiV1CredentialsArchiveCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_credentials_archive_create_description_error_component import (
            ApiV1CredentialsArchiveCreateDescriptionErrorComponent,
        )
        from ..models.api_v1_credentials_archive_create_display_name_error_component import (
            ApiV1CredentialsArchiveCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_credentials_archive_create_kind_error_component import (
            ApiV1CredentialsArchiveCreateKindErrorComponent,
        )
        from ..models.api_v1_credentials_archive_create_kubeconfig_error_component import (
            ApiV1CredentialsArchiveCreateKubeconfigErrorComponent,
        )
        from ..models.api_v1_credentials_archive_create_labels_error_component import (
            ApiV1CredentialsArchiveCreateLabelsErrorComponent,
        )
        from ..models.api_v1_credentials_archive_create_name_error_component import (
            ApiV1CredentialsArchiveCreateNameErrorComponent,
        )
        from ..models.api_v1_credentials_archive_create_non_field_errors_error_component import (
            ApiV1CredentialsArchiveCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_credentials_archive_create_platform_service_error_component import (
            ApiV1CredentialsArchiveCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_credentials_archive_create_provider_error_component import (
            ApiV1CredentialsArchiveCreateProviderErrorComponent,
        )
        from ..models.api_v1_credentials_archive_create_provider_id_error_component import (
            ApiV1CredentialsArchiveCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_credentials_archive_create_provider_reference_error_component import (
            ApiV1CredentialsArchiveCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_credentials_archive_create_reconciliation_enabled_error_component import (
            ApiV1CredentialsArchiveCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_credentials_archive_create_sla_availability_error_component import (
            ApiV1CredentialsArchiveCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_credentials_archive_create_sla_target_error_component import (
            ApiV1CredentialsArchiveCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_credentials_archive_create_slo_availability_error_component import (
            ApiV1CredentialsArchiveCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_credentials_archive_create_slo_target_error_component import (
            ApiV1CredentialsArchiveCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_credentials_archive_create_ssh_private_key_error_component import (
            ApiV1CredentialsArchiveCreateSshPrivateKeyErrorComponent,
        )
        from ..models.api_v1_credentials_archive_create_ssh_public_key_error_component import (
            ApiV1CredentialsArchiveCreateSshPublicKeyErrorComponent,
        )
        from ..models.api_v1_credentials_archive_create_target_availability_error_component import (
            ApiV1CredentialsArchiveCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_credentials_archive_create_tolerations_error_component import (
            ApiV1CredentialsArchiveCreateTolerationsErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1CredentialsArchiveCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsArchiveCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsArchiveCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsArchiveCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsArchiveCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsArchiveCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsArchiveCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsArchiveCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsArchiveCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsArchiveCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsArchiveCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsArchiveCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsArchiveCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsArchiveCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsArchiveCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsArchiveCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsArchiveCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsArchiveCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsArchiveCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsArchiveCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsArchiveCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsArchiveCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsArchiveCreateApiEndpointErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsArchiveCreateApiUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsArchiveCreateApiKeyErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsArchiveCreateKubeconfigErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsArchiveCreateSshPrivateKeyErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsArchiveCreateSshPublicKeyErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsArchiveCreateDescriptionErrorComponent):
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
        from ..models.api_v1_credentials_archive_create_annotations_error_component import (
            ApiV1CredentialsArchiveCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_credentials_archive_create_api_endpoint_error_component import (
            ApiV1CredentialsArchiveCreateApiEndpointErrorComponent,
        )
        from ..models.api_v1_credentials_archive_create_api_key_error_component import (
            ApiV1CredentialsArchiveCreateApiKeyErrorComponent,
        )
        from ..models.api_v1_credentials_archive_create_api_user_error_component import (
            ApiV1CredentialsArchiveCreateApiUserErrorComponent,
        )
        from ..models.api_v1_credentials_archive_create_archived_at_error_component import (
            ApiV1CredentialsArchiveCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_credentials_archive_create_archived_error_component import (
            ApiV1CredentialsArchiveCreateArchivedErrorComponent,
        )
        from ..models.api_v1_credentials_archive_create_archived_reason_error_component import (
            ApiV1CredentialsArchiveCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_credentials_archive_create_criticality_error_component import (
            ApiV1CredentialsArchiveCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_credentials_archive_create_debug_mode_error_component import (
            ApiV1CredentialsArchiveCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_credentials_archive_create_description_error_component import (
            ApiV1CredentialsArchiveCreateDescriptionErrorComponent,
        )
        from ..models.api_v1_credentials_archive_create_display_name_error_component import (
            ApiV1CredentialsArchiveCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_credentials_archive_create_kind_error_component import (
            ApiV1CredentialsArchiveCreateKindErrorComponent,
        )
        from ..models.api_v1_credentials_archive_create_kubeconfig_error_component import (
            ApiV1CredentialsArchiveCreateKubeconfigErrorComponent,
        )
        from ..models.api_v1_credentials_archive_create_labels_error_component import (
            ApiV1CredentialsArchiveCreateLabelsErrorComponent,
        )
        from ..models.api_v1_credentials_archive_create_metadata_error_component import (
            ApiV1CredentialsArchiveCreateMetadataErrorComponent,
        )
        from ..models.api_v1_credentials_archive_create_name_error_component import (
            ApiV1CredentialsArchiveCreateNameErrorComponent,
        )
        from ..models.api_v1_credentials_archive_create_non_field_errors_error_component import (
            ApiV1CredentialsArchiveCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_credentials_archive_create_platform_service_error_component import (
            ApiV1CredentialsArchiveCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_credentials_archive_create_provider_error_component import (
            ApiV1CredentialsArchiveCreateProviderErrorComponent,
        )
        from ..models.api_v1_credentials_archive_create_provider_id_error_component import (
            ApiV1CredentialsArchiveCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_credentials_archive_create_provider_reference_error_component import (
            ApiV1CredentialsArchiveCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_credentials_archive_create_reconciliation_enabled_error_component import (
            ApiV1CredentialsArchiveCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_credentials_archive_create_sla_availability_error_component import (
            ApiV1CredentialsArchiveCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_credentials_archive_create_sla_target_error_component import (
            ApiV1CredentialsArchiveCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_credentials_archive_create_slo_availability_error_component import (
            ApiV1CredentialsArchiveCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_credentials_archive_create_slo_target_error_component import (
            ApiV1CredentialsArchiveCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_credentials_archive_create_ssh_private_key_error_component import (
            ApiV1CredentialsArchiveCreateSshPrivateKeyErrorComponent,
        )
        from ..models.api_v1_credentials_archive_create_ssh_public_key_error_component import (
            ApiV1CredentialsArchiveCreateSshPublicKeyErrorComponent,
        )
        from ..models.api_v1_credentials_archive_create_target_availability_error_component import (
            ApiV1CredentialsArchiveCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_credentials_archive_create_tolerations_error_component import (
            ApiV1CredentialsArchiveCreateTolerationsErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1CredentialsArchiveCreateAnnotationsErrorComponent
                | ApiV1CredentialsArchiveCreateApiEndpointErrorComponent
                | ApiV1CredentialsArchiveCreateApiKeyErrorComponent
                | ApiV1CredentialsArchiveCreateApiUserErrorComponent
                | ApiV1CredentialsArchiveCreateArchivedAtErrorComponent
                | ApiV1CredentialsArchiveCreateArchivedErrorComponent
                | ApiV1CredentialsArchiveCreateArchivedReasonErrorComponent
                | ApiV1CredentialsArchiveCreateCriticalityErrorComponent
                | ApiV1CredentialsArchiveCreateDebugModeErrorComponent
                | ApiV1CredentialsArchiveCreateDescriptionErrorComponent
                | ApiV1CredentialsArchiveCreateDisplayNameErrorComponent
                | ApiV1CredentialsArchiveCreateKindErrorComponent
                | ApiV1CredentialsArchiveCreateKubeconfigErrorComponent
                | ApiV1CredentialsArchiveCreateLabelsErrorComponent
                | ApiV1CredentialsArchiveCreateMetadataErrorComponent
                | ApiV1CredentialsArchiveCreateNameErrorComponent
                | ApiV1CredentialsArchiveCreateNonFieldErrorsErrorComponent
                | ApiV1CredentialsArchiveCreatePlatformServiceErrorComponent
                | ApiV1CredentialsArchiveCreateProviderErrorComponent
                | ApiV1CredentialsArchiveCreateProviderIdErrorComponent
                | ApiV1CredentialsArchiveCreateProviderReferenceErrorComponent
                | ApiV1CredentialsArchiveCreateReconciliationEnabledErrorComponent
                | ApiV1CredentialsArchiveCreateSlaAvailabilityErrorComponent
                | ApiV1CredentialsArchiveCreateSlaTargetErrorComponent
                | ApiV1CredentialsArchiveCreateSloAvailabilityErrorComponent
                | ApiV1CredentialsArchiveCreateSloTargetErrorComponent
                | ApiV1CredentialsArchiveCreateSshPrivateKeyErrorComponent
                | ApiV1CredentialsArchiveCreateSshPublicKeyErrorComponent
                | ApiV1CredentialsArchiveCreateTargetAvailabilityErrorComponent
                | ApiV1CredentialsArchiveCreateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_archive_create_error_type_0 = (
                        ApiV1CredentialsArchiveCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_archive_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_archive_create_error_type_1 = (
                        ApiV1CredentialsArchiveCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_archive_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_archive_create_error_type_2 = (
                        ApiV1CredentialsArchiveCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_archive_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_archive_create_error_type_3 = (
                        ApiV1CredentialsArchiveCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_archive_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_archive_create_error_type_4 = (
                        ApiV1CredentialsArchiveCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_archive_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_archive_create_error_type_5 = (
                        ApiV1CredentialsArchiveCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_archive_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_archive_create_error_type_6 = (
                        ApiV1CredentialsArchiveCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_archive_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_archive_create_error_type_7 = (
                        ApiV1CredentialsArchiveCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_archive_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_archive_create_error_type_8 = (
                        ApiV1CredentialsArchiveCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_archive_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_archive_create_error_type_9 = (
                        ApiV1CredentialsArchiveCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_archive_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_archive_create_error_type_10 = (
                        ApiV1CredentialsArchiveCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_archive_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_archive_create_error_type_11 = (
                        ApiV1CredentialsArchiveCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_archive_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_archive_create_error_type_12 = (
                        ApiV1CredentialsArchiveCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_archive_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_archive_create_error_type_13 = (
                        ApiV1CredentialsArchiveCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_archive_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_archive_create_error_type_14 = (
                        ApiV1CredentialsArchiveCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_archive_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_archive_create_error_type_15 = (
                        ApiV1CredentialsArchiveCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_archive_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_archive_create_error_type_16 = (
                        ApiV1CredentialsArchiveCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_archive_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_archive_create_error_type_17 = (
                        ApiV1CredentialsArchiveCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_archive_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_archive_create_error_type_18 = (
                        ApiV1CredentialsArchiveCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_archive_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_archive_create_error_type_19 = (
                        ApiV1CredentialsArchiveCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_archive_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_archive_create_error_type_20 = (
                        ApiV1CredentialsArchiveCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_archive_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_archive_create_error_type_21 = (
                        ApiV1CredentialsArchiveCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_archive_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_archive_create_error_type_22 = (
                        ApiV1CredentialsArchiveCreateApiEndpointErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_archive_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_archive_create_error_type_23 = (
                        ApiV1CredentialsArchiveCreateApiUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_archive_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_archive_create_error_type_24 = (
                        ApiV1CredentialsArchiveCreateApiKeyErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_archive_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_archive_create_error_type_25 = (
                        ApiV1CredentialsArchiveCreateKubeconfigErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_archive_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_archive_create_error_type_26 = (
                        ApiV1CredentialsArchiveCreateSshPrivateKeyErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_archive_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_archive_create_error_type_27 = (
                        ApiV1CredentialsArchiveCreateSshPublicKeyErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_archive_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_archive_create_error_type_28 = (
                        ApiV1CredentialsArchiveCreateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_archive_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_credentials_archive_create_error_type_29 = (
                    ApiV1CredentialsArchiveCreateMetadataErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_credentials_archive_create_error_type_29

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_credentials_archive_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_credentials_archive_create_validation_error.additional_properties = d
        return api_v1_credentials_archive_create_validation_error

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
