from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_credentials_reconcile_create_annotations_error_component import (
        ApiV1CredentialsReconcileCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_credentials_reconcile_create_api_endpoint_error_component import (
        ApiV1CredentialsReconcileCreateApiEndpointErrorComponent,
    )
    from ..models.api_v1_credentials_reconcile_create_api_key_error_component import (
        ApiV1CredentialsReconcileCreateApiKeyErrorComponent,
    )
    from ..models.api_v1_credentials_reconcile_create_api_user_error_component import (
        ApiV1CredentialsReconcileCreateApiUserErrorComponent,
    )
    from ..models.api_v1_credentials_reconcile_create_archived_at_error_component import (
        ApiV1CredentialsReconcileCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_credentials_reconcile_create_archived_error_component import (
        ApiV1CredentialsReconcileCreateArchivedErrorComponent,
    )
    from ..models.api_v1_credentials_reconcile_create_archived_reason_error_component import (
        ApiV1CredentialsReconcileCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_credentials_reconcile_create_criticality_error_component import (
        ApiV1CredentialsReconcileCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_credentials_reconcile_create_debug_mode_error_component import (
        ApiV1CredentialsReconcileCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_credentials_reconcile_create_description_error_component import (
        ApiV1CredentialsReconcileCreateDescriptionErrorComponent,
    )
    from ..models.api_v1_credentials_reconcile_create_display_name_error_component import (
        ApiV1CredentialsReconcileCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_credentials_reconcile_create_kind_error_component import (
        ApiV1CredentialsReconcileCreateKindErrorComponent,
    )
    from ..models.api_v1_credentials_reconcile_create_kubeconfig_error_component import (
        ApiV1CredentialsReconcileCreateKubeconfigErrorComponent,
    )
    from ..models.api_v1_credentials_reconcile_create_labels_error_component import (
        ApiV1CredentialsReconcileCreateLabelsErrorComponent,
    )
    from ..models.api_v1_credentials_reconcile_create_metadata_error_component import (
        ApiV1CredentialsReconcileCreateMetadataErrorComponent,
    )
    from ..models.api_v1_credentials_reconcile_create_name_error_component import (
        ApiV1CredentialsReconcileCreateNameErrorComponent,
    )
    from ..models.api_v1_credentials_reconcile_create_non_field_errors_error_component import (
        ApiV1CredentialsReconcileCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_credentials_reconcile_create_platform_service_error_component import (
        ApiV1CredentialsReconcileCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_credentials_reconcile_create_provider_error_component import (
        ApiV1CredentialsReconcileCreateProviderErrorComponent,
    )
    from ..models.api_v1_credentials_reconcile_create_provider_id_error_component import (
        ApiV1CredentialsReconcileCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_credentials_reconcile_create_provider_reference_error_component import (
        ApiV1CredentialsReconcileCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_credentials_reconcile_create_reconciliation_enabled_error_component import (
        ApiV1CredentialsReconcileCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_credentials_reconcile_create_sla_availability_error_component import (
        ApiV1CredentialsReconcileCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_credentials_reconcile_create_sla_target_error_component import (
        ApiV1CredentialsReconcileCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_credentials_reconcile_create_slo_availability_error_component import (
        ApiV1CredentialsReconcileCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_credentials_reconcile_create_slo_target_error_component import (
        ApiV1CredentialsReconcileCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_credentials_reconcile_create_ssh_private_key_error_component import (
        ApiV1CredentialsReconcileCreateSshPrivateKeyErrorComponent,
    )
    from ..models.api_v1_credentials_reconcile_create_ssh_public_key_error_component import (
        ApiV1CredentialsReconcileCreateSshPublicKeyErrorComponent,
    )
    from ..models.api_v1_credentials_reconcile_create_target_availability_error_component import (
        ApiV1CredentialsReconcileCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_credentials_reconcile_create_tolerations_error_component import (
        ApiV1CredentialsReconcileCreateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1CredentialsReconcileCreateValidationError")


@_attrs_define
class ApiV1CredentialsReconcileCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1CredentialsReconcileCreateAnnotationsErrorComponent |
            ApiV1CredentialsReconcileCreateApiEndpointErrorComponent | ApiV1CredentialsReconcileCreateApiKeyErrorComponent |
            ApiV1CredentialsReconcileCreateApiUserErrorComponent | ApiV1CredentialsReconcileCreateArchivedAtErrorComponent |
            ApiV1CredentialsReconcileCreateArchivedErrorComponent |
            ApiV1CredentialsReconcileCreateArchivedReasonErrorComponent |
            ApiV1CredentialsReconcileCreateCriticalityErrorComponent |
            ApiV1CredentialsReconcileCreateDebugModeErrorComponent |
            ApiV1CredentialsReconcileCreateDescriptionErrorComponent |
            ApiV1CredentialsReconcileCreateDisplayNameErrorComponent | ApiV1CredentialsReconcileCreateKindErrorComponent |
            ApiV1CredentialsReconcileCreateKubeconfigErrorComponent | ApiV1CredentialsReconcileCreateLabelsErrorComponent |
            ApiV1CredentialsReconcileCreateMetadataErrorComponent | ApiV1CredentialsReconcileCreateNameErrorComponent |
            ApiV1CredentialsReconcileCreateNonFieldErrorsErrorComponent |
            ApiV1CredentialsReconcileCreatePlatformServiceErrorComponent |
            ApiV1CredentialsReconcileCreateProviderErrorComponent | ApiV1CredentialsReconcileCreateProviderIdErrorComponent
            | ApiV1CredentialsReconcileCreateProviderReferenceErrorComponent |
            ApiV1CredentialsReconcileCreateReconciliationEnabledErrorComponent |
            ApiV1CredentialsReconcileCreateSlaAvailabilityErrorComponent |
            ApiV1CredentialsReconcileCreateSlaTargetErrorComponent |
            ApiV1CredentialsReconcileCreateSloAvailabilityErrorComponent |
            ApiV1CredentialsReconcileCreateSloTargetErrorComponent |
            ApiV1CredentialsReconcileCreateSshPrivateKeyErrorComponent |
            ApiV1CredentialsReconcileCreateSshPublicKeyErrorComponent |
            ApiV1CredentialsReconcileCreateTargetAvailabilityErrorComponent |
            ApiV1CredentialsReconcileCreateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1CredentialsReconcileCreateAnnotationsErrorComponent
        | ApiV1CredentialsReconcileCreateApiEndpointErrorComponent
        | ApiV1CredentialsReconcileCreateApiKeyErrorComponent
        | ApiV1CredentialsReconcileCreateApiUserErrorComponent
        | ApiV1CredentialsReconcileCreateArchivedAtErrorComponent
        | ApiV1CredentialsReconcileCreateArchivedErrorComponent
        | ApiV1CredentialsReconcileCreateArchivedReasonErrorComponent
        | ApiV1CredentialsReconcileCreateCriticalityErrorComponent
        | ApiV1CredentialsReconcileCreateDebugModeErrorComponent
        | ApiV1CredentialsReconcileCreateDescriptionErrorComponent
        | ApiV1CredentialsReconcileCreateDisplayNameErrorComponent
        | ApiV1CredentialsReconcileCreateKindErrorComponent
        | ApiV1CredentialsReconcileCreateKubeconfigErrorComponent
        | ApiV1CredentialsReconcileCreateLabelsErrorComponent
        | ApiV1CredentialsReconcileCreateMetadataErrorComponent
        | ApiV1CredentialsReconcileCreateNameErrorComponent
        | ApiV1CredentialsReconcileCreateNonFieldErrorsErrorComponent
        | ApiV1CredentialsReconcileCreatePlatformServiceErrorComponent
        | ApiV1CredentialsReconcileCreateProviderErrorComponent
        | ApiV1CredentialsReconcileCreateProviderIdErrorComponent
        | ApiV1CredentialsReconcileCreateProviderReferenceErrorComponent
        | ApiV1CredentialsReconcileCreateReconciliationEnabledErrorComponent
        | ApiV1CredentialsReconcileCreateSlaAvailabilityErrorComponent
        | ApiV1CredentialsReconcileCreateSlaTargetErrorComponent
        | ApiV1CredentialsReconcileCreateSloAvailabilityErrorComponent
        | ApiV1CredentialsReconcileCreateSloTargetErrorComponent
        | ApiV1CredentialsReconcileCreateSshPrivateKeyErrorComponent
        | ApiV1CredentialsReconcileCreateSshPublicKeyErrorComponent
        | ApiV1CredentialsReconcileCreateTargetAvailabilityErrorComponent
        | ApiV1CredentialsReconcileCreateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_credentials_reconcile_create_annotations_error_component import (
            ApiV1CredentialsReconcileCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_credentials_reconcile_create_api_endpoint_error_component import (
            ApiV1CredentialsReconcileCreateApiEndpointErrorComponent,
        )
        from ..models.api_v1_credentials_reconcile_create_api_key_error_component import (
            ApiV1CredentialsReconcileCreateApiKeyErrorComponent,
        )
        from ..models.api_v1_credentials_reconcile_create_api_user_error_component import (
            ApiV1CredentialsReconcileCreateApiUserErrorComponent,
        )
        from ..models.api_v1_credentials_reconcile_create_archived_at_error_component import (
            ApiV1CredentialsReconcileCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_credentials_reconcile_create_archived_error_component import (
            ApiV1CredentialsReconcileCreateArchivedErrorComponent,
        )
        from ..models.api_v1_credentials_reconcile_create_archived_reason_error_component import (
            ApiV1CredentialsReconcileCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_credentials_reconcile_create_criticality_error_component import (
            ApiV1CredentialsReconcileCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_credentials_reconcile_create_debug_mode_error_component import (
            ApiV1CredentialsReconcileCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_credentials_reconcile_create_description_error_component import (
            ApiV1CredentialsReconcileCreateDescriptionErrorComponent,
        )
        from ..models.api_v1_credentials_reconcile_create_display_name_error_component import (
            ApiV1CredentialsReconcileCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_credentials_reconcile_create_kind_error_component import (
            ApiV1CredentialsReconcileCreateKindErrorComponent,
        )
        from ..models.api_v1_credentials_reconcile_create_kubeconfig_error_component import (
            ApiV1CredentialsReconcileCreateKubeconfigErrorComponent,
        )
        from ..models.api_v1_credentials_reconcile_create_labels_error_component import (
            ApiV1CredentialsReconcileCreateLabelsErrorComponent,
        )
        from ..models.api_v1_credentials_reconcile_create_name_error_component import (
            ApiV1CredentialsReconcileCreateNameErrorComponent,
        )
        from ..models.api_v1_credentials_reconcile_create_non_field_errors_error_component import (
            ApiV1CredentialsReconcileCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_credentials_reconcile_create_platform_service_error_component import (
            ApiV1CredentialsReconcileCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_credentials_reconcile_create_provider_error_component import (
            ApiV1CredentialsReconcileCreateProviderErrorComponent,
        )
        from ..models.api_v1_credentials_reconcile_create_provider_id_error_component import (
            ApiV1CredentialsReconcileCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_credentials_reconcile_create_provider_reference_error_component import (
            ApiV1CredentialsReconcileCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_credentials_reconcile_create_reconciliation_enabled_error_component import (
            ApiV1CredentialsReconcileCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_credentials_reconcile_create_sla_availability_error_component import (
            ApiV1CredentialsReconcileCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_credentials_reconcile_create_sla_target_error_component import (
            ApiV1CredentialsReconcileCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_credentials_reconcile_create_slo_availability_error_component import (
            ApiV1CredentialsReconcileCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_credentials_reconcile_create_slo_target_error_component import (
            ApiV1CredentialsReconcileCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_credentials_reconcile_create_ssh_private_key_error_component import (
            ApiV1CredentialsReconcileCreateSshPrivateKeyErrorComponent,
        )
        from ..models.api_v1_credentials_reconcile_create_ssh_public_key_error_component import (
            ApiV1CredentialsReconcileCreateSshPublicKeyErrorComponent,
        )
        from ..models.api_v1_credentials_reconcile_create_target_availability_error_component import (
            ApiV1CredentialsReconcileCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_credentials_reconcile_create_tolerations_error_component import (
            ApiV1CredentialsReconcileCreateTolerationsErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1CredentialsReconcileCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsReconcileCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsReconcileCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsReconcileCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsReconcileCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsReconcileCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsReconcileCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsReconcileCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsReconcileCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsReconcileCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsReconcileCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsReconcileCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsReconcileCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsReconcileCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsReconcileCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsReconcileCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsReconcileCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsReconcileCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsReconcileCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsReconcileCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsReconcileCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsReconcileCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsReconcileCreateApiEndpointErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsReconcileCreateApiUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsReconcileCreateApiKeyErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsReconcileCreateKubeconfigErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsReconcileCreateSshPrivateKeyErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsReconcileCreateSshPublicKeyErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsReconcileCreateDescriptionErrorComponent):
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
        from ..models.api_v1_credentials_reconcile_create_annotations_error_component import (
            ApiV1CredentialsReconcileCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_credentials_reconcile_create_api_endpoint_error_component import (
            ApiV1CredentialsReconcileCreateApiEndpointErrorComponent,
        )
        from ..models.api_v1_credentials_reconcile_create_api_key_error_component import (
            ApiV1CredentialsReconcileCreateApiKeyErrorComponent,
        )
        from ..models.api_v1_credentials_reconcile_create_api_user_error_component import (
            ApiV1CredentialsReconcileCreateApiUserErrorComponent,
        )
        from ..models.api_v1_credentials_reconcile_create_archived_at_error_component import (
            ApiV1CredentialsReconcileCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_credentials_reconcile_create_archived_error_component import (
            ApiV1CredentialsReconcileCreateArchivedErrorComponent,
        )
        from ..models.api_v1_credentials_reconcile_create_archived_reason_error_component import (
            ApiV1CredentialsReconcileCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_credentials_reconcile_create_criticality_error_component import (
            ApiV1CredentialsReconcileCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_credentials_reconcile_create_debug_mode_error_component import (
            ApiV1CredentialsReconcileCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_credentials_reconcile_create_description_error_component import (
            ApiV1CredentialsReconcileCreateDescriptionErrorComponent,
        )
        from ..models.api_v1_credentials_reconcile_create_display_name_error_component import (
            ApiV1CredentialsReconcileCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_credentials_reconcile_create_kind_error_component import (
            ApiV1CredentialsReconcileCreateKindErrorComponent,
        )
        from ..models.api_v1_credentials_reconcile_create_kubeconfig_error_component import (
            ApiV1CredentialsReconcileCreateKubeconfigErrorComponent,
        )
        from ..models.api_v1_credentials_reconcile_create_labels_error_component import (
            ApiV1CredentialsReconcileCreateLabelsErrorComponent,
        )
        from ..models.api_v1_credentials_reconcile_create_metadata_error_component import (
            ApiV1CredentialsReconcileCreateMetadataErrorComponent,
        )
        from ..models.api_v1_credentials_reconcile_create_name_error_component import (
            ApiV1CredentialsReconcileCreateNameErrorComponent,
        )
        from ..models.api_v1_credentials_reconcile_create_non_field_errors_error_component import (
            ApiV1CredentialsReconcileCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_credentials_reconcile_create_platform_service_error_component import (
            ApiV1CredentialsReconcileCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_credentials_reconcile_create_provider_error_component import (
            ApiV1CredentialsReconcileCreateProviderErrorComponent,
        )
        from ..models.api_v1_credentials_reconcile_create_provider_id_error_component import (
            ApiV1CredentialsReconcileCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_credentials_reconcile_create_provider_reference_error_component import (
            ApiV1CredentialsReconcileCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_credentials_reconcile_create_reconciliation_enabled_error_component import (
            ApiV1CredentialsReconcileCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_credentials_reconcile_create_sla_availability_error_component import (
            ApiV1CredentialsReconcileCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_credentials_reconcile_create_sla_target_error_component import (
            ApiV1CredentialsReconcileCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_credentials_reconcile_create_slo_availability_error_component import (
            ApiV1CredentialsReconcileCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_credentials_reconcile_create_slo_target_error_component import (
            ApiV1CredentialsReconcileCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_credentials_reconcile_create_ssh_private_key_error_component import (
            ApiV1CredentialsReconcileCreateSshPrivateKeyErrorComponent,
        )
        from ..models.api_v1_credentials_reconcile_create_ssh_public_key_error_component import (
            ApiV1CredentialsReconcileCreateSshPublicKeyErrorComponent,
        )
        from ..models.api_v1_credentials_reconcile_create_target_availability_error_component import (
            ApiV1CredentialsReconcileCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_credentials_reconcile_create_tolerations_error_component import (
            ApiV1CredentialsReconcileCreateTolerationsErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1CredentialsReconcileCreateAnnotationsErrorComponent
                | ApiV1CredentialsReconcileCreateApiEndpointErrorComponent
                | ApiV1CredentialsReconcileCreateApiKeyErrorComponent
                | ApiV1CredentialsReconcileCreateApiUserErrorComponent
                | ApiV1CredentialsReconcileCreateArchivedAtErrorComponent
                | ApiV1CredentialsReconcileCreateArchivedErrorComponent
                | ApiV1CredentialsReconcileCreateArchivedReasonErrorComponent
                | ApiV1CredentialsReconcileCreateCriticalityErrorComponent
                | ApiV1CredentialsReconcileCreateDebugModeErrorComponent
                | ApiV1CredentialsReconcileCreateDescriptionErrorComponent
                | ApiV1CredentialsReconcileCreateDisplayNameErrorComponent
                | ApiV1CredentialsReconcileCreateKindErrorComponent
                | ApiV1CredentialsReconcileCreateKubeconfigErrorComponent
                | ApiV1CredentialsReconcileCreateLabelsErrorComponent
                | ApiV1CredentialsReconcileCreateMetadataErrorComponent
                | ApiV1CredentialsReconcileCreateNameErrorComponent
                | ApiV1CredentialsReconcileCreateNonFieldErrorsErrorComponent
                | ApiV1CredentialsReconcileCreatePlatformServiceErrorComponent
                | ApiV1CredentialsReconcileCreateProviderErrorComponent
                | ApiV1CredentialsReconcileCreateProviderIdErrorComponent
                | ApiV1CredentialsReconcileCreateProviderReferenceErrorComponent
                | ApiV1CredentialsReconcileCreateReconciliationEnabledErrorComponent
                | ApiV1CredentialsReconcileCreateSlaAvailabilityErrorComponent
                | ApiV1CredentialsReconcileCreateSlaTargetErrorComponent
                | ApiV1CredentialsReconcileCreateSloAvailabilityErrorComponent
                | ApiV1CredentialsReconcileCreateSloTargetErrorComponent
                | ApiV1CredentialsReconcileCreateSshPrivateKeyErrorComponent
                | ApiV1CredentialsReconcileCreateSshPublicKeyErrorComponent
                | ApiV1CredentialsReconcileCreateTargetAvailabilityErrorComponent
                | ApiV1CredentialsReconcileCreateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_reconcile_create_error_type_0 = (
                        ApiV1CredentialsReconcileCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_reconcile_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_reconcile_create_error_type_1 = (
                        ApiV1CredentialsReconcileCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_reconcile_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_reconcile_create_error_type_2 = (
                        ApiV1CredentialsReconcileCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_reconcile_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_reconcile_create_error_type_3 = (
                        ApiV1CredentialsReconcileCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_reconcile_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_reconcile_create_error_type_4 = (
                        ApiV1CredentialsReconcileCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_reconcile_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_reconcile_create_error_type_5 = (
                        ApiV1CredentialsReconcileCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_reconcile_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_reconcile_create_error_type_6 = (
                        ApiV1CredentialsReconcileCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_reconcile_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_reconcile_create_error_type_7 = (
                        ApiV1CredentialsReconcileCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_reconcile_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_reconcile_create_error_type_8 = (
                        ApiV1CredentialsReconcileCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_reconcile_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_reconcile_create_error_type_9 = (
                        ApiV1CredentialsReconcileCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_reconcile_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_reconcile_create_error_type_10 = (
                        ApiV1CredentialsReconcileCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_reconcile_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_reconcile_create_error_type_11 = (
                        ApiV1CredentialsReconcileCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_reconcile_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_reconcile_create_error_type_12 = (
                        ApiV1CredentialsReconcileCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_reconcile_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_reconcile_create_error_type_13 = (
                        ApiV1CredentialsReconcileCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_reconcile_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_reconcile_create_error_type_14 = (
                        ApiV1CredentialsReconcileCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_reconcile_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_reconcile_create_error_type_15 = (
                        ApiV1CredentialsReconcileCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_reconcile_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_reconcile_create_error_type_16 = (
                        ApiV1CredentialsReconcileCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_reconcile_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_reconcile_create_error_type_17 = (
                        ApiV1CredentialsReconcileCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_reconcile_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_reconcile_create_error_type_18 = (
                        ApiV1CredentialsReconcileCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_reconcile_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_reconcile_create_error_type_19 = (
                        ApiV1CredentialsReconcileCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_reconcile_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_reconcile_create_error_type_20 = (
                        ApiV1CredentialsReconcileCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_reconcile_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_reconcile_create_error_type_21 = (
                        ApiV1CredentialsReconcileCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_reconcile_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_reconcile_create_error_type_22 = (
                        ApiV1CredentialsReconcileCreateApiEndpointErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_reconcile_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_reconcile_create_error_type_23 = (
                        ApiV1CredentialsReconcileCreateApiUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_reconcile_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_reconcile_create_error_type_24 = (
                        ApiV1CredentialsReconcileCreateApiKeyErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_reconcile_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_reconcile_create_error_type_25 = (
                        ApiV1CredentialsReconcileCreateKubeconfigErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_reconcile_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_reconcile_create_error_type_26 = (
                        ApiV1CredentialsReconcileCreateSshPrivateKeyErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_reconcile_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_reconcile_create_error_type_27 = (
                        ApiV1CredentialsReconcileCreateSshPublicKeyErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_reconcile_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_reconcile_create_error_type_28 = (
                        ApiV1CredentialsReconcileCreateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_reconcile_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_credentials_reconcile_create_error_type_29 = (
                    ApiV1CredentialsReconcileCreateMetadataErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_credentials_reconcile_create_error_type_29

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_credentials_reconcile_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_credentials_reconcile_create_validation_error.additional_properties = d
        return api_v1_credentials_reconcile_create_validation_error

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
