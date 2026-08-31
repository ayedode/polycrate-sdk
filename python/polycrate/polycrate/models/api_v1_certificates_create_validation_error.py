from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_certificates_create_annotations_error_component import (
        ApiV1CertificatesCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_certificates_create_archived_at_error_component import (
        ApiV1CertificatesCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_certificates_create_archived_error_component import (
        ApiV1CertificatesCreateArchivedErrorComponent,
    )
    from ..models.api_v1_certificates_create_archived_reason_error_component import (
        ApiV1CertificatesCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_certificates_create_cert_manager_status_error_component import (
        ApiV1CertificatesCreateCertManagerStatusErrorComponent,
    )
    from ..models.api_v1_certificates_create_certificate_status_error_component import (
        ApiV1CertificatesCreateCertificateStatusErrorComponent,
    )
    from ..models.api_v1_certificates_create_challenge_reason_error_component import (
        ApiV1CertificatesCreateChallengeReasonErrorComponent,
    )
    from ..models.api_v1_certificates_create_criticality_error_component import (
        ApiV1CertificatesCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_certificates_create_current_challenge_status_error_component import (
        ApiV1CertificatesCreateCurrentChallengeStatusErrorComponent,
    )
    from ..models.api_v1_certificates_create_current_challenge_type_error_component import (
        ApiV1CertificatesCreateCurrentChallengeTypeErrorComponent,
    )
    from ..models.api_v1_certificates_create_debug_mode_error_component import (
        ApiV1CertificatesCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_certificates_create_display_name_error_component import (
        ApiV1CertificatesCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_certificates_create_dns_names_error_component import (
        ApiV1CertificatesCreateDnsNamesErrorComponent,
    )
    from ..models.api_v1_certificates_create_failure_reason_error_component import (
        ApiV1CertificatesCreateFailureReasonErrorComponent,
    )
    from ..models.api_v1_certificates_create_ip_addresses_error_component import (
        ApiV1CertificatesCreateIpAddressesErrorComponent,
    )
    from ..models.api_v1_certificates_create_is_ready_error_component import (
        ApiV1CertificatesCreateIsReadyErrorComponent,
    )
    from ..models.api_v1_certificates_create_issuer_group_error_component import (
        ApiV1CertificatesCreateIssuerGroupErrorComponent,
    )
    from ..models.api_v1_certificates_create_issuer_kind_error_component import (
        ApiV1CertificatesCreateIssuerKindErrorComponent,
    )
    from ..models.api_v1_certificates_create_issuer_name_error_component import (
        ApiV1CertificatesCreateIssuerNameErrorComponent,
    )
    from ..models.api_v1_certificates_create_k8s_cluster_error_component import (
        ApiV1CertificatesCreateK8SClusterErrorComponent,
    )
    from ..models.api_v1_certificates_create_kind_error_component import ApiV1CertificatesCreateKindErrorComponent
    from ..models.api_v1_certificates_create_labels_error_component import ApiV1CertificatesCreateLabelsErrorComponent
    from ..models.api_v1_certificates_create_last_failure_time_error_component import (
        ApiV1CertificatesCreateLastFailureTimeErrorComponent,
    )
    from ..models.api_v1_certificates_create_last_synced_from_cluster_error_component import (
        ApiV1CertificatesCreateLastSyncedFromClusterErrorComponent,
    )
    from ..models.api_v1_certificates_create_metadata_error_component import (
        ApiV1CertificatesCreateMetadataErrorComponent,
    )
    from ..models.api_v1_certificates_create_name_error_component import ApiV1CertificatesCreateNameErrorComponent
    from ..models.api_v1_certificates_create_namespace_error_component import (
        ApiV1CertificatesCreateNamespaceErrorComponent,
    )
    from ..models.api_v1_certificates_create_non_field_errors_error_component import (
        ApiV1CertificatesCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_certificates_create_not_after_error_component import (
        ApiV1CertificatesCreateNotAfterErrorComponent,
    )
    from ..models.api_v1_certificates_create_not_before_error_component import (
        ApiV1CertificatesCreateNotBeforeErrorComponent,
    )
    from ..models.api_v1_certificates_create_platform_service_error_component import (
        ApiV1CertificatesCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_certificates_create_provider_error_component import (
        ApiV1CertificatesCreateProviderErrorComponent,
    )
    from ..models.api_v1_certificates_create_provider_id_error_component import (
        ApiV1CertificatesCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_certificates_create_provider_reference_error_component import (
        ApiV1CertificatesCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_certificates_create_reconciliation_enabled_error_component import (
        ApiV1CertificatesCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_certificates_create_renewal_time_error_component import (
        ApiV1CertificatesCreateRenewalTimeErrorComponent,
    )
    from ..models.api_v1_certificates_create_secret_name_error_component import (
        ApiV1CertificatesCreateSecretNameErrorComponent,
    )
    from ..models.api_v1_certificates_create_sla_availability_error_component import (
        ApiV1CertificatesCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_certificates_create_sla_target_error_component import (
        ApiV1CertificatesCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_certificates_create_slo_availability_error_component import (
        ApiV1CertificatesCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_certificates_create_slo_target_error_component import (
        ApiV1CertificatesCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_certificates_create_target_availability_error_component import (
        ApiV1CertificatesCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_certificates_create_tolerations_error_component import (
        ApiV1CertificatesCreateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1CertificatesCreateValidationError")


@_attrs_define
class ApiV1CertificatesCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1CertificatesCreateAnnotationsErrorComponent | ApiV1CertificatesCreateArchivedAtErrorComponent
            | ApiV1CertificatesCreateArchivedErrorComponent | ApiV1CertificatesCreateArchivedReasonErrorComponent |
            ApiV1CertificatesCreateCertificateStatusErrorComponent | ApiV1CertificatesCreateCertManagerStatusErrorComponent
            | ApiV1CertificatesCreateChallengeReasonErrorComponent | ApiV1CertificatesCreateCriticalityErrorComponent |
            ApiV1CertificatesCreateCurrentChallengeStatusErrorComponent |
            ApiV1CertificatesCreateCurrentChallengeTypeErrorComponent | ApiV1CertificatesCreateDebugModeErrorComponent |
            ApiV1CertificatesCreateDisplayNameErrorComponent | ApiV1CertificatesCreateDnsNamesErrorComponent |
            ApiV1CertificatesCreateFailureReasonErrorComponent | ApiV1CertificatesCreateIpAddressesErrorComponent |
            ApiV1CertificatesCreateIsReadyErrorComponent | ApiV1CertificatesCreateIssuerGroupErrorComponent |
            ApiV1CertificatesCreateIssuerKindErrorComponent | ApiV1CertificatesCreateIssuerNameErrorComponent |
            ApiV1CertificatesCreateK8SClusterErrorComponent | ApiV1CertificatesCreateKindErrorComponent |
            ApiV1CertificatesCreateLabelsErrorComponent | ApiV1CertificatesCreateLastFailureTimeErrorComponent |
            ApiV1CertificatesCreateLastSyncedFromClusterErrorComponent | ApiV1CertificatesCreateMetadataErrorComponent |
            ApiV1CertificatesCreateNameErrorComponent | ApiV1CertificatesCreateNamespaceErrorComponent |
            ApiV1CertificatesCreateNonFieldErrorsErrorComponent | ApiV1CertificatesCreateNotAfterErrorComponent |
            ApiV1CertificatesCreateNotBeforeErrorComponent | ApiV1CertificatesCreatePlatformServiceErrorComponent |
            ApiV1CertificatesCreateProviderErrorComponent | ApiV1CertificatesCreateProviderIdErrorComponent |
            ApiV1CertificatesCreateProviderReferenceErrorComponent |
            ApiV1CertificatesCreateReconciliationEnabledErrorComponent | ApiV1CertificatesCreateRenewalTimeErrorComponent |
            ApiV1CertificatesCreateSecretNameErrorComponent | ApiV1CertificatesCreateSlaAvailabilityErrorComponent |
            ApiV1CertificatesCreateSlaTargetErrorComponent | ApiV1CertificatesCreateSloAvailabilityErrorComponent |
            ApiV1CertificatesCreateSloTargetErrorComponent | ApiV1CertificatesCreateTargetAvailabilityErrorComponent |
            ApiV1CertificatesCreateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1CertificatesCreateAnnotationsErrorComponent
        | ApiV1CertificatesCreateArchivedAtErrorComponent
        | ApiV1CertificatesCreateArchivedErrorComponent
        | ApiV1CertificatesCreateArchivedReasonErrorComponent
        | ApiV1CertificatesCreateCertificateStatusErrorComponent
        | ApiV1CertificatesCreateCertManagerStatusErrorComponent
        | ApiV1CertificatesCreateChallengeReasonErrorComponent
        | ApiV1CertificatesCreateCriticalityErrorComponent
        | ApiV1CertificatesCreateCurrentChallengeStatusErrorComponent
        | ApiV1CertificatesCreateCurrentChallengeTypeErrorComponent
        | ApiV1CertificatesCreateDebugModeErrorComponent
        | ApiV1CertificatesCreateDisplayNameErrorComponent
        | ApiV1CertificatesCreateDnsNamesErrorComponent
        | ApiV1CertificatesCreateFailureReasonErrorComponent
        | ApiV1CertificatesCreateIpAddressesErrorComponent
        | ApiV1CertificatesCreateIsReadyErrorComponent
        | ApiV1CertificatesCreateIssuerGroupErrorComponent
        | ApiV1CertificatesCreateIssuerKindErrorComponent
        | ApiV1CertificatesCreateIssuerNameErrorComponent
        | ApiV1CertificatesCreateK8SClusterErrorComponent
        | ApiV1CertificatesCreateKindErrorComponent
        | ApiV1CertificatesCreateLabelsErrorComponent
        | ApiV1CertificatesCreateLastFailureTimeErrorComponent
        | ApiV1CertificatesCreateLastSyncedFromClusterErrorComponent
        | ApiV1CertificatesCreateMetadataErrorComponent
        | ApiV1CertificatesCreateNameErrorComponent
        | ApiV1CertificatesCreateNamespaceErrorComponent
        | ApiV1CertificatesCreateNonFieldErrorsErrorComponent
        | ApiV1CertificatesCreateNotAfterErrorComponent
        | ApiV1CertificatesCreateNotBeforeErrorComponent
        | ApiV1CertificatesCreatePlatformServiceErrorComponent
        | ApiV1CertificatesCreateProviderErrorComponent
        | ApiV1CertificatesCreateProviderIdErrorComponent
        | ApiV1CertificatesCreateProviderReferenceErrorComponent
        | ApiV1CertificatesCreateReconciliationEnabledErrorComponent
        | ApiV1CertificatesCreateRenewalTimeErrorComponent
        | ApiV1CertificatesCreateSecretNameErrorComponent
        | ApiV1CertificatesCreateSlaAvailabilityErrorComponent
        | ApiV1CertificatesCreateSlaTargetErrorComponent
        | ApiV1CertificatesCreateSloAvailabilityErrorComponent
        | ApiV1CertificatesCreateSloTargetErrorComponent
        | ApiV1CertificatesCreateTargetAvailabilityErrorComponent
        | ApiV1CertificatesCreateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_certificates_create_annotations_error_component import (
            ApiV1CertificatesCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_certificates_create_archived_at_error_component import (
            ApiV1CertificatesCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_certificates_create_archived_error_component import (
            ApiV1CertificatesCreateArchivedErrorComponent,
        )
        from ..models.api_v1_certificates_create_archived_reason_error_component import (
            ApiV1CertificatesCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_certificates_create_cert_manager_status_error_component import (
            ApiV1CertificatesCreateCertManagerStatusErrorComponent,
        )
        from ..models.api_v1_certificates_create_certificate_status_error_component import (
            ApiV1CertificatesCreateCertificateStatusErrorComponent,
        )
        from ..models.api_v1_certificates_create_challenge_reason_error_component import (
            ApiV1CertificatesCreateChallengeReasonErrorComponent,
        )
        from ..models.api_v1_certificates_create_criticality_error_component import (
            ApiV1CertificatesCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_certificates_create_current_challenge_status_error_component import (
            ApiV1CertificatesCreateCurrentChallengeStatusErrorComponent,
        )
        from ..models.api_v1_certificates_create_current_challenge_type_error_component import (
            ApiV1CertificatesCreateCurrentChallengeTypeErrorComponent,
        )
        from ..models.api_v1_certificates_create_debug_mode_error_component import (
            ApiV1CertificatesCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_certificates_create_display_name_error_component import (
            ApiV1CertificatesCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_certificates_create_dns_names_error_component import (
            ApiV1CertificatesCreateDnsNamesErrorComponent,
        )
        from ..models.api_v1_certificates_create_failure_reason_error_component import (
            ApiV1CertificatesCreateFailureReasonErrorComponent,
        )
        from ..models.api_v1_certificates_create_ip_addresses_error_component import (
            ApiV1CertificatesCreateIpAddressesErrorComponent,
        )
        from ..models.api_v1_certificates_create_is_ready_error_component import (
            ApiV1CertificatesCreateIsReadyErrorComponent,
        )
        from ..models.api_v1_certificates_create_issuer_group_error_component import (
            ApiV1CertificatesCreateIssuerGroupErrorComponent,
        )
        from ..models.api_v1_certificates_create_issuer_kind_error_component import (
            ApiV1CertificatesCreateIssuerKindErrorComponent,
        )
        from ..models.api_v1_certificates_create_issuer_name_error_component import (
            ApiV1CertificatesCreateIssuerNameErrorComponent,
        )
        from ..models.api_v1_certificates_create_k8s_cluster_error_component import (
            ApiV1CertificatesCreateK8SClusterErrorComponent,
        )
        from ..models.api_v1_certificates_create_kind_error_component import ApiV1CertificatesCreateKindErrorComponent
        from ..models.api_v1_certificates_create_labels_error_component import (
            ApiV1CertificatesCreateLabelsErrorComponent,
        )
        from ..models.api_v1_certificates_create_last_failure_time_error_component import (
            ApiV1CertificatesCreateLastFailureTimeErrorComponent,
        )
        from ..models.api_v1_certificates_create_last_synced_from_cluster_error_component import (
            ApiV1CertificatesCreateLastSyncedFromClusterErrorComponent,
        )
        from ..models.api_v1_certificates_create_name_error_component import ApiV1CertificatesCreateNameErrorComponent
        from ..models.api_v1_certificates_create_namespace_error_component import (
            ApiV1CertificatesCreateNamespaceErrorComponent,
        )
        from ..models.api_v1_certificates_create_non_field_errors_error_component import (
            ApiV1CertificatesCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_certificates_create_not_after_error_component import (
            ApiV1CertificatesCreateNotAfterErrorComponent,
        )
        from ..models.api_v1_certificates_create_not_before_error_component import (
            ApiV1CertificatesCreateNotBeforeErrorComponent,
        )
        from ..models.api_v1_certificates_create_platform_service_error_component import (
            ApiV1CertificatesCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_certificates_create_provider_error_component import (
            ApiV1CertificatesCreateProviderErrorComponent,
        )
        from ..models.api_v1_certificates_create_provider_id_error_component import (
            ApiV1CertificatesCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_certificates_create_provider_reference_error_component import (
            ApiV1CertificatesCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_certificates_create_reconciliation_enabled_error_component import (
            ApiV1CertificatesCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_certificates_create_renewal_time_error_component import (
            ApiV1CertificatesCreateRenewalTimeErrorComponent,
        )
        from ..models.api_v1_certificates_create_secret_name_error_component import (
            ApiV1CertificatesCreateSecretNameErrorComponent,
        )
        from ..models.api_v1_certificates_create_sla_availability_error_component import (
            ApiV1CertificatesCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_certificates_create_sla_target_error_component import (
            ApiV1CertificatesCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_certificates_create_slo_availability_error_component import (
            ApiV1CertificatesCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_certificates_create_slo_target_error_component import (
            ApiV1CertificatesCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_certificates_create_target_availability_error_component import (
            ApiV1CertificatesCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_certificates_create_tolerations_error_component import (
            ApiV1CertificatesCreateTolerationsErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1CertificatesCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesCreateSecretNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesCreateNamespaceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesCreateDnsNamesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesCreateIpAddressesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesCreateIssuerNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesCreateIssuerKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesCreateIssuerGroupErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesCreateNotBeforeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesCreateNotAfterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesCreateRenewalTimeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesCreateCertificateStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesCreateIsReadyErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesCreateCurrentChallengeTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesCreateCurrentChallengeStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesCreateChallengeReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesCreateLastFailureTimeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesCreateFailureReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesCreateLastSyncedFromClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesCreateCertManagerStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesCreateK8SClusterErrorComponent):
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
        from ..models.api_v1_certificates_create_annotations_error_component import (
            ApiV1CertificatesCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_certificates_create_archived_at_error_component import (
            ApiV1CertificatesCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_certificates_create_archived_error_component import (
            ApiV1CertificatesCreateArchivedErrorComponent,
        )
        from ..models.api_v1_certificates_create_archived_reason_error_component import (
            ApiV1CertificatesCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_certificates_create_cert_manager_status_error_component import (
            ApiV1CertificatesCreateCertManagerStatusErrorComponent,
        )
        from ..models.api_v1_certificates_create_certificate_status_error_component import (
            ApiV1CertificatesCreateCertificateStatusErrorComponent,
        )
        from ..models.api_v1_certificates_create_challenge_reason_error_component import (
            ApiV1CertificatesCreateChallengeReasonErrorComponent,
        )
        from ..models.api_v1_certificates_create_criticality_error_component import (
            ApiV1CertificatesCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_certificates_create_current_challenge_status_error_component import (
            ApiV1CertificatesCreateCurrentChallengeStatusErrorComponent,
        )
        from ..models.api_v1_certificates_create_current_challenge_type_error_component import (
            ApiV1CertificatesCreateCurrentChallengeTypeErrorComponent,
        )
        from ..models.api_v1_certificates_create_debug_mode_error_component import (
            ApiV1CertificatesCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_certificates_create_display_name_error_component import (
            ApiV1CertificatesCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_certificates_create_dns_names_error_component import (
            ApiV1CertificatesCreateDnsNamesErrorComponent,
        )
        from ..models.api_v1_certificates_create_failure_reason_error_component import (
            ApiV1CertificatesCreateFailureReasonErrorComponent,
        )
        from ..models.api_v1_certificates_create_ip_addresses_error_component import (
            ApiV1CertificatesCreateIpAddressesErrorComponent,
        )
        from ..models.api_v1_certificates_create_is_ready_error_component import (
            ApiV1CertificatesCreateIsReadyErrorComponent,
        )
        from ..models.api_v1_certificates_create_issuer_group_error_component import (
            ApiV1CertificatesCreateIssuerGroupErrorComponent,
        )
        from ..models.api_v1_certificates_create_issuer_kind_error_component import (
            ApiV1CertificatesCreateIssuerKindErrorComponent,
        )
        from ..models.api_v1_certificates_create_issuer_name_error_component import (
            ApiV1CertificatesCreateIssuerNameErrorComponent,
        )
        from ..models.api_v1_certificates_create_k8s_cluster_error_component import (
            ApiV1CertificatesCreateK8SClusterErrorComponent,
        )
        from ..models.api_v1_certificates_create_kind_error_component import ApiV1CertificatesCreateKindErrorComponent
        from ..models.api_v1_certificates_create_labels_error_component import (
            ApiV1CertificatesCreateLabelsErrorComponent,
        )
        from ..models.api_v1_certificates_create_last_failure_time_error_component import (
            ApiV1CertificatesCreateLastFailureTimeErrorComponent,
        )
        from ..models.api_v1_certificates_create_last_synced_from_cluster_error_component import (
            ApiV1CertificatesCreateLastSyncedFromClusterErrorComponent,
        )
        from ..models.api_v1_certificates_create_metadata_error_component import (
            ApiV1CertificatesCreateMetadataErrorComponent,
        )
        from ..models.api_v1_certificates_create_name_error_component import ApiV1CertificatesCreateNameErrorComponent
        from ..models.api_v1_certificates_create_namespace_error_component import (
            ApiV1CertificatesCreateNamespaceErrorComponent,
        )
        from ..models.api_v1_certificates_create_non_field_errors_error_component import (
            ApiV1CertificatesCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_certificates_create_not_after_error_component import (
            ApiV1CertificatesCreateNotAfterErrorComponent,
        )
        from ..models.api_v1_certificates_create_not_before_error_component import (
            ApiV1CertificatesCreateNotBeforeErrorComponent,
        )
        from ..models.api_v1_certificates_create_platform_service_error_component import (
            ApiV1CertificatesCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_certificates_create_provider_error_component import (
            ApiV1CertificatesCreateProviderErrorComponent,
        )
        from ..models.api_v1_certificates_create_provider_id_error_component import (
            ApiV1CertificatesCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_certificates_create_provider_reference_error_component import (
            ApiV1CertificatesCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_certificates_create_reconciliation_enabled_error_component import (
            ApiV1CertificatesCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_certificates_create_renewal_time_error_component import (
            ApiV1CertificatesCreateRenewalTimeErrorComponent,
        )
        from ..models.api_v1_certificates_create_secret_name_error_component import (
            ApiV1CertificatesCreateSecretNameErrorComponent,
        )
        from ..models.api_v1_certificates_create_sla_availability_error_component import (
            ApiV1CertificatesCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_certificates_create_sla_target_error_component import (
            ApiV1CertificatesCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_certificates_create_slo_availability_error_component import (
            ApiV1CertificatesCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_certificates_create_slo_target_error_component import (
            ApiV1CertificatesCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_certificates_create_target_availability_error_component import (
            ApiV1CertificatesCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_certificates_create_tolerations_error_component import (
            ApiV1CertificatesCreateTolerationsErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1CertificatesCreateAnnotationsErrorComponent
                | ApiV1CertificatesCreateArchivedAtErrorComponent
                | ApiV1CertificatesCreateArchivedErrorComponent
                | ApiV1CertificatesCreateArchivedReasonErrorComponent
                | ApiV1CertificatesCreateCertificateStatusErrorComponent
                | ApiV1CertificatesCreateCertManagerStatusErrorComponent
                | ApiV1CertificatesCreateChallengeReasonErrorComponent
                | ApiV1CertificatesCreateCriticalityErrorComponent
                | ApiV1CertificatesCreateCurrentChallengeStatusErrorComponent
                | ApiV1CertificatesCreateCurrentChallengeTypeErrorComponent
                | ApiV1CertificatesCreateDebugModeErrorComponent
                | ApiV1CertificatesCreateDisplayNameErrorComponent
                | ApiV1CertificatesCreateDnsNamesErrorComponent
                | ApiV1CertificatesCreateFailureReasonErrorComponent
                | ApiV1CertificatesCreateIpAddressesErrorComponent
                | ApiV1CertificatesCreateIsReadyErrorComponent
                | ApiV1CertificatesCreateIssuerGroupErrorComponent
                | ApiV1CertificatesCreateIssuerKindErrorComponent
                | ApiV1CertificatesCreateIssuerNameErrorComponent
                | ApiV1CertificatesCreateK8SClusterErrorComponent
                | ApiV1CertificatesCreateKindErrorComponent
                | ApiV1CertificatesCreateLabelsErrorComponent
                | ApiV1CertificatesCreateLastFailureTimeErrorComponent
                | ApiV1CertificatesCreateLastSyncedFromClusterErrorComponent
                | ApiV1CertificatesCreateMetadataErrorComponent
                | ApiV1CertificatesCreateNameErrorComponent
                | ApiV1CertificatesCreateNamespaceErrorComponent
                | ApiV1CertificatesCreateNonFieldErrorsErrorComponent
                | ApiV1CertificatesCreateNotAfterErrorComponent
                | ApiV1CertificatesCreateNotBeforeErrorComponent
                | ApiV1CertificatesCreatePlatformServiceErrorComponent
                | ApiV1CertificatesCreateProviderErrorComponent
                | ApiV1CertificatesCreateProviderIdErrorComponent
                | ApiV1CertificatesCreateProviderReferenceErrorComponent
                | ApiV1CertificatesCreateReconciliationEnabledErrorComponent
                | ApiV1CertificatesCreateRenewalTimeErrorComponent
                | ApiV1CertificatesCreateSecretNameErrorComponent
                | ApiV1CertificatesCreateSlaAvailabilityErrorComponent
                | ApiV1CertificatesCreateSlaTargetErrorComponent
                | ApiV1CertificatesCreateSloAvailabilityErrorComponent
                | ApiV1CertificatesCreateSloTargetErrorComponent
                | ApiV1CertificatesCreateTargetAvailabilityErrorComponent
                | ApiV1CertificatesCreateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_create_error_type_0 = (
                        ApiV1CertificatesCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_create_error_type_1 = (
                        ApiV1CertificatesCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_create_error_type_2 = (
                        ApiV1CertificatesCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_create_error_type_3 = (
                        ApiV1CertificatesCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_create_error_type_4 = (
                        ApiV1CertificatesCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_create_error_type_5 = (
                        ApiV1CertificatesCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_create_error_type_6 = (
                        ApiV1CertificatesCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_create_error_type_7 = (
                        ApiV1CertificatesCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_create_error_type_8 = (
                        ApiV1CertificatesCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_create_error_type_9 = (
                        ApiV1CertificatesCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_create_error_type_10 = (
                        ApiV1CertificatesCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_create_error_type_11 = (
                        ApiV1CertificatesCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_create_error_type_12 = (
                        ApiV1CertificatesCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_create_error_type_13 = (
                        ApiV1CertificatesCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_create_error_type_14 = (
                        ApiV1CertificatesCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_create_error_type_15 = (
                        ApiV1CertificatesCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_create_error_type_16 = (
                        ApiV1CertificatesCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_create_error_type_17 = (
                        ApiV1CertificatesCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_create_error_type_18 = (
                        ApiV1CertificatesCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_create_error_type_19 = (
                        ApiV1CertificatesCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_create_error_type_20 = (
                        ApiV1CertificatesCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_create_error_type_21 = (
                        ApiV1CertificatesCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_create_error_type_22 = (
                        ApiV1CertificatesCreateSecretNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_create_error_type_23 = (
                        ApiV1CertificatesCreateNamespaceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_create_error_type_24 = (
                        ApiV1CertificatesCreateDnsNamesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_create_error_type_25 = (
                        ApiV1CertificatesCreateIpAddressesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_create_error_type_26 = (
                        ApiV1CertificatesCreateIssuerNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_create_error_type_27 = (
                        ApiV1CertificatesCreateIssuerKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_create_error_type_28 = (
                        ApiV1CertificatesCreateIssuerGroupErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_create_error_type_29 = (
                        ApiV1CertificatesCreateNotBeforeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_create_error_type_30 = (
                        ApiV1CertificatesCreateNotAfterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_create_error_type_31 = (
                        ApiV1CertificatesCreateRenewalTimeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_create_error_type_32 = (
                        ApiV1CertificatesCreateCertificateStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_create_error_type_33 = (
                        ApiV1CertificatesCreateIsReadyErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_create_error_type_34 = (
                        ApiV1CertificatesCreateCurrentChallengeTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_create_error_type_35 = (
                        ApiV1CertificatesCreateCurrentChallengeStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_create_error_type_36 = (
                        ApiV1CertificatesCreateChallengeReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_create_error_type_37 = (
                        ApiV1CertificatesCreateLastFailureTimeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_create_error_type_38 = (
                        ApiV1CertificatesCreateFailureReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_create_error_type_39 = (
                        ApiV1CertificatesCreateLastSyncedFromClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_create_error_type_40 = (
                        ApiV1CertificatesCreateCertManagerStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_create_error_type_41 = (
                        ApiV1CertificatesCreateK8SClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_certificates_create_error_type_42 = (
                    ApiV1CertificatesCreateMetadataErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_certificates_create_error_type_42

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_certificates_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_certificates_create_validation_error.additional_properties = d
        return api_v1_certificates_create_validation_error

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
