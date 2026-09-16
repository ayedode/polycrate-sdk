from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_credentials_discover_create_annotations_error_component import (
        ApiV1CredentialsDiscoverCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_credentials_discover_create_api_endpoint_error_component import (
        ApiV1CredentialsDiscoverCreateApiEndpointErrorComponent,
    )
    from ..models.api_v1_credentials_discover_create_api_key_error_component import (
        ApiV1CredentialsDiscoverCreateApiKeyErrorComponent,
    )
    from ..models.api_v1_credentials_discover_create_api_user_error_component import (
        ApiV1CredentialsDiscoverCreateApiUserErrorComponent,
    )
    from ..models.api_v1_credentials_discover_create_archived_at_error_component import (
        ApiV1CredentialsDiscoverCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_credentials_discover_create_archived_error_component import (
        ApiV1CredentialsDiscoverCreateArchivedErrorComponent,
    )
    from ..models.api_v1_credentials_discover_create_archived_reason_error_component import (
        ApiV1CredentialsDiscoverCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_credentials_discover_create_criticality_error_component import (
        ApiV1CredentialsDiscoverCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_credentials_discover_create_debug_mode_error_component import (
        ApiV1CredentialsDiscoverCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_credentials_discover_create_description_error_component import (
        ApiV1CredentialsDiscoverCreateDescriptionErrorComponent,
    )
    from ..models.api_v1_credentials_discover_create_display_name_error_component import (
        ApiV1CredentialsDiscoverCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_credentials_discover_create_kind_error_component import (
        ApiV1CredentialsDiscoverCreateKindErrorComponent,
    )
    from ..models.api_v1_credentials_discover_create_kubeconfig_error_component import (
        ApiV1CredentialsDiscoverCreateKubeconfigErrorComponent,
    )
    from ..models.api_v1_credentials_discover_create_labels_error_component import (
        ApiV1CredentialsDiscoverCreateLabelsErrorComponent,
    )
    from ..models.api_v1_credentials_discover_create_metadata_error_component import (
        ApiV1CredentialsDiscoverCreateMetadataErrorComponent,
    )
    from ..models.api_v1_credentials_discover_create_name_error_component import (
        ApiV1CredentialsDiscoverCreateNameErrorComponent,
    )
    from ..models.api_v1_credentials_discover_create_non_field_errors_error_component import (
        ApiV1CredentialsDiscoverCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_credentials_discover_create_platform_service_error_component import (
        ApiV1CredentialsDiscoverCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_credentials_discover_create_provider_error_component import (
        ApiV1CredentialsDiscoverCreateProviderErrorComponent,
    )
    from ..models.api_v1_credentials_discover_create_provider_id_error_component import (
        ApiV1CredentialsDiscoverCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_credentials_discover_create_provider_reference_error_component import (
        ApiV1CredentialsDiscoverCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_credentials_discover_create_reconciliation_enabled_error_component import (
        ApiV1CredentialsDiscoverCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_credentials_discover_create_sla_availability_error_component import (
        ApiV1CredentialsDiscoverCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_credentials_discover_create_sla_target_error_component import (
        ApiV1CredentialsDiscoverCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_credentials_discover_create_slo_availability_error_component import (
        ApiV1CredentialsDiscoverCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_credentials_discover_create_slo_target_error_component import (
        ApiV1CredentialsDiscoverCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_credentials_discover_create_ssh_private_key_error_component import (
        ApiV1CredentialsDiscoverCreateSshPrivateKeyErrorComponent,
    )
    from ..models.api_v1_credentials_discover_create_ssh_public_key_error_component import (
        ApiV1CredentialsDiscoverCreateSshPublicKeyErrorComponent,
    )
    from ..models.api_v1_credentials_discover_create_target_availability_error_component import (
        ApiV1CredentialsDiscoverCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_credentials_discover_create_tolerations_error_component import (
        ApiV1CredentialsDiscoverCreateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1CredentialsDiscoverCreateValidationError")


@_attrs_define
class ApiV1CredentialsDiscoverCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1CredentialsDiscoverCreateAnnotationsErrorComponent |
            ApiV1CredentialsDiscoverCreateApiEndpointErrorComponent | ApiV1CredentialsDiscoverCreateApiKeyErrorComponent |
            ApiV1CredentialsDiscoverCreateApiUserErrorComponent | ApiV1CredentialsDiscoverCreateArchivedAtErrorComponent |
            ApiV1CredentialsDiscoverCreateArchivedErrorComponent |
            ApiV1CredentialsDiscoverCreateArchivedReasonErrorComponent |
            ApiV1CredentialsDiscoverCreateCriticalityErrorComponent | ApiV1CredentialsDiscoverCreateDebugModeErrorComponent
            | ApiV1CredentialsDiscoverCreateDescriptionErrorComponent |
            ApiV1CredentialsDiscoverCreateDisplayNameErrorComponent | ApiV1CredentialsDiscoverCreateKindErrorComponent |
            ApiV1CredentialsDiscoverCreateKubeconfigErrorComponent | ApiV1CredentialsDiscoverCreateLabelsErrorComponent |
            ApiV1CredentialsDiscoverCreateMetadataErrorComponent | ApiV1CredentialsDiscoverCreateNameErrorComponent |
            ApiV1CredentialsDiscoverCreateNonFieldErrorsErrorComponent |
            ApiV1CredentialsDiscoverCreatePlatformServiceErrorComponent |
            ApiV1CredentialsDiscoverCreateProviderErrorComponent | ApiV1CredentialsDiscoverCreateProviderIdErrorComponent |
            ApiV1CredentialsDiscoverCreateProviderReferenceErrorComponent |
            ApiV1CredentialsDiscoverCreateReconciliationEnabledErrorComponent |
            ApiV1CredentialsDiscoverCreateSlaAvailabilityErrorComponent |
            ApiV1CredentialsDiscoverCreateSlaTargetErrorComponent |
            ApiV1CredentialsDiscoverCreateSloAvailabilityErrorComponent |
            ApiV1CredentialsDiscoverCreateSloTargetErrorComponent |
            ApiV1CredentialsDiscoverCreateSshPrivateKeyErrorComponent |
            ApiV1CredentialsDiscoverCreateSshPublicKeyErrorComponent |
            ApiV1CredentialsDiscoverCreateTargetAvailabilityErrorComponent |
            ApiV1CredentialsDiscoverCreateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1CredentialsDiscoverCreateAnnotationsErrorComponent
        | ApiV1CredentialsDiscoverCreateApiEndpointErrorComponent
        | ApiV1CredentialsDiscoverCreateApiKeyErrorComponent
        | ApiV1CredentialsDiscoverCreateApiUserErrorComponent
        | ApiV1CredentialsDiscoverCreateArchivedAtErrorComponent
        | ApiV1CredentialsDiscoverCreateArchivedErrorComponent
        | ApiV1CredentialsDiscoverCreateArchivedReasonErrorComponent
        | ApiV1CredentialsDiscoverCreateCriticalityErrorComponent
        | ApiV1CredentialsDiscoverCreateDebugModeErrorComponent
        | ApiV1CredentialsDiscoverCreateDescriptionErrorComponent
        | ApiV1CredentialsDiscoverCreateDisplayNameErrorComponent
        | ApiV1CredentialsDiscoverCreateKindErrorComponent
        | ApiV1CredentialsDiscoverCreateKubeconfigErrorComponent
        | ApiV1CredentialsDiscoverCreateLabelsErrorComponent
        | ApiV1CredentialsDiscoverCreateMetadataErrorComponent
        | ApiV1CredentialsDiscoverCreateNameErrorComponent
        | ApiV1CredentialsDiscoverCreateNonFieldErrorsErrorComponent
        | ApiV1CredentialsDiscoverCreatePlatformServiceErrorComponent
        | ApiV1CredentialsDiscoverCreateProviderErrorComponent
        | ApiV1CredentialsDiscoverCreateProviderIdErrorComponent
        | ApiV1CredentialsDiscoverCreateProviderReferenceErrorComponent
        | ApiV1CredentialsDiscoverCreateReconciliationEnabledErrorComponent
        | ApiV1CredentialsDiscoverCreateSlaAvailabilityErrorComponent
        | ApiV1CredentialsDiscoverCreateSlaTargetErrorComponent
        | ApiV1CredentialsDiscoverCreateSloAvailabilityErrorComponent
        | ApiV1CredentialsDiscoverCreateSloTargetErrorComponent
        | ApiV1CredentialsDiscoverCreateSshPrivateKeyErrorComponent
        | ApiV1CredentialsDiscoverCreateSshPublicKeyErrorComponent
        | ApiV1CredentialsDiscoverCreateTargetAvailabilityErrorComponent
        | ApiV1CredentialsDiscoverCreateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_credentials_discover_create_annotations_error_component import (
            ApiV1CredentialsDiscoverCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_discover_create_api_endpoint_error_component import (
            ApiV1CredentialsDiscoverCreateApiEndpointErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_discover_create_api_key_error_component import (
            ApiV1CredentialsDiscoverCreateApiKeyErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_discover_create_api_user_error_component import (
            ApiV1CredentialsDiscoverCreateApiUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_discover_create_archived_at_error_component import (
            ApiV1CredentialsDiscoverCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_discover_create_archived_error_component import (
            ApiV1CredentialsDiscoverCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_discover_create_archived_reason_error_component import (
            ApiV1CredentialsDiscoverCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_discover_create_criticality_error_component import (
            ApiV1CredentialsDiscoverCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_discover_create_debug_mode_error_component import (
            ApiV1CredentialsDiscoverCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_discover_create_description_error_component import (
            ApiV1CredentialsDiscoverCreateDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_discover_create_display_name_error_component import (
            ApiV1CredentialsDiscoverCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_discover_create_kind_error_component import (
            ApiV1CredentialsDiscoverCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_discover_create_kubeconfig_error_component import (
            ApiV1CredentialsDiscoverCreateKubeconfigErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_discover_create_labels_error_component import (
            ApiV1CredentialsDiscoverCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_discover_create_name_error_component import (
            ApiV1CredentialsDiscoverCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_discover_create_non_field_errors_error_component import (
            ApiV1CredentialsDiscoverCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_discover_create_platform_service_error_component import (
            ApiV1CredentialsDiscoverCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_discover_create_provider_error_component import (
            ApiV1CredentialsDiscoverCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_discover_create_provider_id_error_component import (
            ApiV1CredentialsDiscoverCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_discover_create_provider_reference_error_component import (
            ApiV1CredentialsDiscoverCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_discover_create_reconciliation_enabled_error_component import (
            ApiV1CredentialsDiscoverCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_discover_create_sla_availability_error_component import (
            ApiV1CredentialsDiscoverCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_discover_create_sla_target_error_component import (
            ApiV1CredentialsDiscoverCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_discover_create_slo_availability_error_component import (
            ApiV1CredentialsDiscoverCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_discover_create_slo_target_error_component import (
            ApiV1CredentialsDiscoverCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_discover_create_ssh_private_key_error_component import (
            ApiV1CredentialsDiscoverCreateSshPrivateKeyErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_discover_create_ssh_public_key_error_component import (
            ApiV1CredentialsDiscoverCreateSshPublicKeyErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_discover_create_target_availability_error_component import (
            ApiV1CredentialsDiscoverCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_discover_create_tolerations_error_component import (
            ApiV1CredentialsDiscoverCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1CredentialsDiscoverCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsDiscoverCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsDiscoverCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsDiscoverCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsDiscoverCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsDiscoverCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsDiscoverCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsDiscoverCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsDiscoverCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsDiscoverCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsDiscoverCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsDiscoverCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsDiscoverCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsDiscoverCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsDiscoverCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsDiscoverCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsDiscoverCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsDiscoverCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsDiscoverCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsDiscoverCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsDiscoverCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsDiscoverCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsDiscoverCreateApiEndpointErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsDiscoverCreateApiUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsDiscoverCreateApiKeyErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsDiscoverCreateKubeconfigErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsDiscoverCreateSshPrivateKeyErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsDiscoverCreateSshPublicKeyErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CredentialsDiscoverCreateDescriptionErrorComponent):
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
        from ..models.api_v1_credentials_discover_create_annotations_error_component import (
            ApiV1CredentialsDiscoverCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_discover_create_api_endpoint_error_component import (
            ApiV1CredentialsDiscoverCreateApiEndpointErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_discover_create_api_key_error_component import (
            ApiV1CredentialsDiscoverCreateApiKeyErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_discover_create_api_user_error_component import (
            ApiV1CredentialsDiscoverCreateApiUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_discover_create_archived_at_error_component import (
            ApiV1CredentialsDiscoverCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_discover_create_archived_error_component import (
            ApiV1CredentialsDiscoverCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_discover_create_archived_reason_error_component import (
            ApiV1CredentialsDiscoverCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_discover_create_criticality_error_component import (
            ApiV1CredentialsDiscoverCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_discover_create_debug_mode_error_component import (
            ApiV1CredentialsDiscoverCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_discover_create_description_error_component import (
            ApiV1CredentialsDiscoverCreateDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_discover_create_display_name_error_component import (
            ApiV1CredentialsDiscoverCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_discover_create_kind_error_component import (
            ApiV1CredentialsDiscoverCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_discover_create_kubeconfig_error_component import (
            ApiV1CredentialsDiscoverCreateKubeconfigErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_discover_create_labels_error_component import (
            ApiV1CredentialsDiscoverCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_discover_create_metadata_error_component import (
            ApiV1CredentialsDiscoverCreateMetadataErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_discover_create_name_error_component import (
            ApiV1CredentialsDiscoverCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_discover_create_non_field_errors_error_component import (
            ApiV1CredentialsDiscoverCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_discover_create_platform_service_error_component import (
            ApiV1CredentialsDiscoverCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_discover_create_provider_error_component import (
            ApiV1CredentialsDiscoverCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_discover_create_provider_id_error_component import (
            ApiV1CredentialsDiscoverCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_discover_create_provider_reference_error_component import (
            ApiV1CredentialsDiscoverCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_discover_create_reconciliation_enabled_error_component import (
            ApiV1CredentialsDiscoverCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_discover_create_sla_availability_error_component import (
            ApiV1CredentialsDiscoverCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_discover_create_sla_target_error_component import (
            ApiV1CredentialsDiscoverCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_discover_create_slo_availability_error_component import (
            ApiV1CredentialsDiscoverCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_discover_create_slo_target_error_component import (
            ApiV1CredentialsDiscoverCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_discover_create_ssh_private_key_error_component import (
            ApiV1CredentialsDiscoverCreateSshPrivateKeyErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_discover_create_ssh_public_key_error_component import (
            ApiV1CredentialsDiscoverCreateSshPublicKeyErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_discover_create_target_availability_error_component import (
            ApiV1CredentialsDiscoverCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_credentials_discover_create_tolerations_error_component import (
            ApiV1CredentialsDiscoverCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1CredentialsDiscoverCreateAnnotationsErrorComponent
                | ApiV1CredentialsDiscoverCreateApiEndpointErrorComponent
                | ApiV1CredentialsDiscoverCreateApiKeyErrorComponent
                | ApiV1CredentialsDiscoverCreateApiUserErrorComponent
                | ApiV1CredentialsDiscoverCreateArchivedAtErrorComponent
                | ApiV1CredentialsDiscoverCreateArchivedErrorComponent
                | ApiV1CredentialsDiscoverCreateArchivedReasonErrorComponent
                | ApiV1CredentialsDiscoverCreateCriticalityErrorComponent
                | ApiV1CredentialsDiscoverCreateDebugModeErrorComponent
                | ApiV1CredentialsDiscoverCreateDescriptionErrorComponent
                | ApiV1CredentialsDiscoverCreateDisplayNameErrorComponent
                | ApiV1CredentialsDiscoverCreateKindErrorComponent
                | ApiV1CredentialsDiscoverCreateKubeconfigErrorComponent
                | ApiV1CredentialsDiscoverCreateLabelsErrorComponent
                | ApiV1CredentialsDiscoverCreateMetadataErrorComponent
                | ApiV1CredentialsDiscoverCreateNameErrorComponent
                | ApiV1CredentialsDiscoverCreateNonFieldErrorsErrorComponent
                | ApiV1CredentialsDiscoverCreatePlatformServiceErrorComponent
                | ApiV1CredentialsDiscoverCreateProviderErrorComponent
                | ApiV1CredentialsDiscoverCreateProviderIdErrorComponent
                | ApiV1CredentialsDiscoverCreateProviderReferenceErrorComponent
                | ApiV1CredentialsDiscoverCreateReconciliationEnabledErrorComponent
                | ApiV1CredentialsDiscoverCreateSlaAvailabilityErrorComponent
                | ApiV1CredentialsDiscoverCreateSlaTargetErrorComponent
                | ApiV1CredentialsDiscoverCreateSloAvailabilityErrorComponent
                | ApiV1CredentialsDiscoverCreateSloTargetErrorComponent
                | ApiV1CredentialsDiscoverCreateSshPrivateKeyErrorComponent
                | ApiV1CredentialsDiscoverCreateSshPublicKeyErrorComponent
                | ApiV1CredentialsDiscoverCreateTargetAvailabilityErrorComponent
                | ApiV1CredentialsDiscoverCreateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_discover_create_error_type_0 = (
                        ApiV1CredentialsDiscoverCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_discover_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_discover_create_error_type_1 = (
                        ApiV1CredentialsDiscoverCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_discover_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_discover_create_error_type_2 = (
                        ApiV1CredentialsDiscoverCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_discover_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_discover_create_error_type_3 = (
                        ApiV1CredentialsDiscoverCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_discover_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_discover_create_error_type_4 = (
                        ApiV1CredentialsDiscoverCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_discover_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_discover_create_error_type_5 = (
                        ApiV1CredentialsDiscoverCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_discover_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_discover_create_error_type_6 = (
                        ApiV1CredentialsDiscoverCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_discover_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_discover_create_error_type_7 = (
                        ApiV1CredentialsDiscoverCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_discover_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_discover_create_error_type_8 = (
                        ApiV1CredentialsDiscoverCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_discover_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_discover_create_error_type_9 = (
                        ApiV1CredentialsDiscoverCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_discover_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_discover_create_error_type_10 = (
                        ApiV1CredentialsDiscoverCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_discover_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_discover_create_error_type_11 = (
                        ApiV1CredentialsDiscoverCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_discover_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_discover_create_error_type_12 = (
                        ApiV1CredentialsDiscoverCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_discover_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_discover_create_error_type_13 = (
                        ApiV1CredentialsDiscoverCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_discover_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_discover_create_error_type_14 = (
                        ApiV1CredentialsDiscoverCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_discover_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_discover_create_error_type_15 = (
                        ApiV1CredentialsDiscoverCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_discover_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_discover_create_error_type_16 = (
                        ApiV1CredentialsDiscoverCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_discover_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_discover_create_error_type_17 = (
                        ApiV1CredentialsDiscoverCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_discover_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_discover_create_error_type_18 = (
                        ApiV1CredentialsDiscoverCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_discover_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_discover_create_error_type_19 = (
                        ApiV1CredentialsDiscoverCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_discover_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_discover_create_error_type_20 = (
                        ApiV1CredentialsDiscoverCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_discover_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_discover_create_error_type_21 = (
                        ApiV1CredentialsDiscoverCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_discover_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_discover_create_error_type_22 = (
                        ApiV1CredentialsDiscoverCreateApiEndpointErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_discover_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_discover_create_error_type_23 = (
                        ApiV1CredentialsDiscoverCreateApiUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_discover_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_discover_create_error_type_24 = (
                        ApiV1CredentialsDiscoverCreateApiKeyErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_discover_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_discover_create_error_type_25 = (
                        ApiV1CredentialsDiscoverCreateKubeconfigErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_discover_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_discover_create_error_type_26 = (
                        ApiV1CredentialsDiscoverCreateSshPrivateKeyErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_discover_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_discover_create_error_type_27 = (
                        ApiV1CredentialsDiscoverCreateSshPublicKeyErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_discover_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_credentials_discover_create_error_type_28 = (
                        ApiV1CredentialsDiscoverCreateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_credentials_discover_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_credentials_discover_create_error_type_29 = (
                    ApiV1CredentialsDiscoverCreateMetadataErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_credentials_discover_create_error_type_29

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_credentials_discover_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_credentials_discover_create_validation_error.additional_properties = d
        return api_v1_credentials_discover_create_validation_error

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
