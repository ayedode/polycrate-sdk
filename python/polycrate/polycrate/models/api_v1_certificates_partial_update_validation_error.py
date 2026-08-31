from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_certificates_partial_update_annotations_error_component import (
        ApiV1CertificatesPartialUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_certificates_partial_update_archived_at_error_component import (
        ApiV1CertificatesPartialUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_certificates_partial_update_archived_error_component import (
        ApiV1CertificatesPartialUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_certificates_partial_update_archived_reason_error_component import (
        ApiV1CertificatesPartialUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_certificates_partial_update_cert_manager_status_error_component import (
        ApiV1CertificatesPartialUpdateCertManagerStatusErrorComponent,
    )
    from ..models.api_v1_certificates_partial_update_certificate_status_error_component import (
        ApiV1CertificatesPartialUpdateCertificateStatusErrorComponent,
    )
    from ..models.api_v1_certificates_partial_update_challenge_reason_error_component import (
        ApiV1CertificatesPartialUpdateChallengeReasonErrorComponent,
    )
    from ..models.api_v1_certificates_partial_update_criticality_error_component import (
        ApiV1CertificatesPartialUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_certificates_partial_update_current_challenge_status_error_component import (
        ApiV1CertificatesPartialUpdateCurrentChallengeStatusErrorComponent,
    )
    from ..models.api_v1_certificates_partial_update_current_challenge_type_error_component import (
        ApiV1CertificatesPartialUpdateCurrentChallengeTypeErrorComponent,
    )
    from ..models.api_v1_certificates_partial_update_debug_mode_error_component import (
        ApiV1CertificatesPartialUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_certificates_partial_update_display_name_error_component import (
        ApiV1CertificatesPartialUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_certificates_partial_update_dns_names_error_component import (
        ApiV1CertificatesPartialUpdateDnsNamesErrorComponent,
    )
    from ..models.api_v1_certificates_partial_update_failure_reason_error_component import (
        ApiV1CertificatesPartialUpdateFailureReasonErrorComponent,
    )
    from ..models.api_v1_certificates_partial_update_ip_addresses_error_component import (
        ApiV1CertificatesPartialUpdateIpAddressesErrorComponent,
    )
    from ..models.api_v1_certificates_partial_update_is_ready_error_component import (
        ApiV1CertificatesPartialUpdateIsReadyErrorComponent,
    )
    from ..models.api_v1_certificates_partial_update_issuer_group_error_component import (
        ApiV1CertificatesPartialUpdateIssuerGroupErrorComponent,
    )
    from ..models.api_v1_certificates_partial_update_issuer_kind_error_component import (
        ApiV1CertificatesPartialUpdateIssuerKindErrorComponent,
    )
    from ..models.api_v1_certificates_partial_update_issuer_name_error_component import (
        ApiV1CertificatesPartialUpdateIssuerNameErrorComponent,
    )
    from ..models.api_v1_certificates_partial_update_k8s_cluster_error_component import (
        ApiV1CertificatesPartialUpdateK8SClusterErrorComponent,
    )
    from ..models.api_v1_certificates_partial_update_kind_error_component import (
        ApiV1CertificatesPartialUpdateKindErrorComponent,
    )
    from ..models.api_v1_certificates_partial_update_labels_error_component import (
        ApiV1CertificatesPartialUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_certificates_partial_update_last_failure_time_error_component import (
        ApiV1CertificatesPartialUpdateLastFailureTimeErrorComponent,
    )
    from ..models.api_v1_certificates_partial_update_last_synced_from_cluster_error_component import (
        ApiV1CertificatesPartialUpdateLastSyncedFromClusterErrorComponent,
    )
    from ..models.api_v1_certificates_partial_update_metadata_error_component import (
        ApiV1CertificatesPartialUpdateMetadataErrorComponent,
    )
    from ..models.api_v1_certificates_partial_update_name_error_component import (
        ApiV1CertificatesPartialUpdateNameErrorComponent,
    )
    from ..models.api_v1_certificates_partial_update_namespace_error_component import (
        ApiV1CertificatesPartialUpdateNamespaceErrorComponent,
    )
    from ..models.api_v1_certificates_partial_update_non_field_errors_error_component import (
        ApiV1CertificatesPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_certificates_partial_update_not_after_error_component import (
        ApiV1CertificatesPartialUpdateNotAfterErrorComponent,
    )
    from ..models.api_v1_certificates_partial_update_not_before_error_component import (
        ApiV1CertificatesPartialUpdateNotBeforeErrorComponent,
    )
    from ..models.api_v1_certificates_partial_update_platform_service_error_component import (
        ApiV1CertificatesPartialUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_certificates_partial_update_provider_error_component import (
        ApiV1CertificatesPartialUpdateProviderErrorComponent,
    )
    from ..models.api_v1_certificates_partial_update_provider_id_error_component import (
        ApiV1CertificatesPartialUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_certificates_partial_update_provider_reference_error_component import (
        ApiV1CertificatesPartialUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_certificates_partial_update_reconciliation_enabled_error_component import (
        ApiV1CertificatesPartialUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_certificates_partial_update_renewal_time_error_component import (
        ApiV1CertificatesPartialUpdateRenewalTimeErrorComponent,
    )
    from ..models.api_v1_certificates_partial_update_secret_name_error_component import (
        ApiV1CertificatesPartialUpdateSecretNameErrorComponent,
    )
    from ..models.api_v1_certificates_partial_update_sla_availability_error_component import (
        ApiV1CertificatesPartialUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_certificates_partial_update_sla_target_error_component import (
        ApiV1CertificatesPartialUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_certificates_partial_update_slo_availability_error_component import (
        ApiV1CertificatesPartialUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_certificates_partial_update_slo_target_error_component import (
        ApiV1CertificatesPartialUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_certificates_partial_update_target_availability_error_component import (
        ApiV1CertificatesPartialUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_certificates_partial_update_tolerations_error_component import (
        ApiV1CertificatesPartialUpdateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1CertificatesPartialUpdateValidationError")


@_attrs_define
class ApiV1CertificatesPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1CertificatesPartialUpdateAnnotationsErrorComponent |
            ApiV1CertificatesPartialUpdateArchivedAtErrorComponent | ApiV1CertificatesPartialUpdateArchivedErrorComponent |
            ApiV1CertificatesPartialUpdateArchivedReasonErrorComponent |
            ApiV1CertificatesPartialUpdateCertificateStatusErrorComponent |
            ApiV1CertificatesPartialUpdateCertManagerStatusErrorComponent |
            ApiV1CertificatesPartialUpdateChallengeReasonErrorComponent |
            ApiV1CertificatesPartialUpdateCriticalityErrorComponent |
            ApiV1CertificatesPartialUpdateCurrentChallengeStatusErrorComponent |
            ApiV1CertificatesPartialUpdateCurrentChallengeTypeErrorComponent |
            ApiV1CertificatesPartialUpdateDebugModeErrorComponent | ApiV1CertificatesPartialUpdateDisplayNameErrorComponent
            | ApiV1CertificatesPartialUpdateDnsNamesErrorComponent |
            ApiV1CertificatesPartialUpdateFailureReasonErrorComponent |
            ApiV1CertificatesPartialUpdateIpAddressesErrorComponent | ApiV1CertificatesPartialUpdateIsReadyErrorComponent |
            ApiV1CertificatesPartialUpdateIssuerGroupErrorComponent | ApiV1CertificatesPartialUpdateIssuerKindErrorComponent
            | ApiV1CertificatesPartialUpdateIssuerNameErrorComponent |
            ApiV1CertificatesPartialUpdateK8SClusterErrorComponent | ApiV1CertificatesPartialUpdateKindErrorComponent |
            ApiV1CertificatesPartialUpdateLabelsErrorComponent | ApiV1CertificatesPartialUpdateLastFailureTimeErrorComponent
            | ApiV1CertificatesPartialUpdateLastSyncedFromClusterErrorComponent |
            ApiV1CertificatesPartialUpdateMetadataErrorComponent | ApiV1CertificatesPartialUpdateNameErrorComponent |
            ApiV1CertificatesPartialUpdateNamespaceErrorComponent |
            ApiV1CertificatesPartialUpdateNonFieldErrorsErrorComponent |
            ApiV1CertificatesPartialUpdateNotAfterErrorComponent | ApiV1CertificatesPartialUpdateNotBeforeErrorComponent |
            ApiV1CertificatesPartialUpdatePlatformServiceErrorComponent |
            ApiV1CertificatesPartialUpdateProviderErrorComponent | ApiV1CertificatesPartialUpdateProviderIdErrorComponent |
            ApiV1CertificatesPartialUpdateProviderReferenceErrorComponent |
            ApiV1CertificatesPartialUpdateReconciliationEnabledErrorComponent |
            ApiV1CertificatesPartialUpdateRenewalTimeErrorComponent | ApiV1CertificatesPartialUpdateSecretNameErrorComponent
            | ApiV1CertificatesPartialUpdateSlaAvailabilityErrorComponent |
            ApiV1CertificatesPartialUpdateSlaTargetErrorComponent |
            ApiV1CertificatesPartialUpdateSloAvailabilityErrorComponent |
            ApiV1CertificatesPartialUpdateSloTargetErrorComponent |
            ApiV1CertificatesPartialUpdateTargetAvailabilityErrorComponent |
            ApiV1CertificatesPartialUpdateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1CertificatesPartialUpdateAnnotationsErrorComponent
        | ApiV1CertificatesPartialUpdateArchivedAtErrorComponent
        | ApiV1CertificatesPartialUpdateArchivedErrorComponent
        | ApiV1CertificatesPartialUpdateArchivedReasonErrorComponent
        | ApiV1CertificatesPartialUpdateCertificateStatusErrorComponent
        | ApiV1CertificatesPartialUpdateCertManagerStatusErrorComponent
        | ApiV1CertificatesPartialUpdateChallengeReasonErrorComponent
        | ApiV1CertificatesPartialUpdateCriticalityErrorComponent
        | ApiV1CertificatesPartialUpdateCurrentChallengeStatusErrorComponent
        | ApiV1CertificatesPartialUpdateCurrentChallengeTypeErrorComponent
        | ApiV1CertificatesPartialUpdateDebugModeErrorComponent
        | ApiV1CertificatesPartialUpdateDisplayNameErrorComponent
        | ApiV1CertificatesPartialUpdateDnsNamesErrorComponent
        | ApiV1CertificatesPartialUpdateFailureReasonErrorComponent
        | ApiV1CertificatesPartialUpdateIpAddressesErrorComponent
        | ApiV1CertificatesPartialUpdateIsReadyErrorComponent
        | ApiV1CertificatesPartialUpdateIssuerGroupErrorComponent
        | ApiV1CertificatesPartialUpdateIssuerKindErrorComponent
        | ApiV1CertificatesPartialUpdateIssuerNameErrorComponent
        | ApiV1CertificatesPartialUpdateK8SClusterErrorComponent
        | ApiV1CertificatesPartialUpdateKindErrorComponent
        | ApiV1CertificatesPartialUpdateLabelsErrorComponent
        | ApiV1CertificatesPartialUpdateLastFailureTimeErrorComponent
        | ApiV1CertificatesPartialUpdateLastSyncedFromClusterErrorComponent
        | ApiV1CertificatesPartialUpdateMetadataErrorComponent
        | ApiV1CertificatesPartialUpdateNameErrorComponent
        | ApiV1CertificatesPartialUpdateNamespaceErrorComponent
        | ApiV1CertificatesPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1CertificatesPartialUpdateNotAfterErrorComponent
        | ApiV1CertificatesPartialUpdateNotBeforeErrorComponent
        | ApiV1CertificatesPartialUpdatePlatformServiceErrorComponent
        | ApiV1CertificatesPartialUpdateProviderErrorComponent
        | ApiV1CertificatesPartialUpdateProviderIdErrorComponent
        | ApiV1CertificatesPartialUpdateProviderReferenceErrorComponent
        | ApiV1CertificatesPartialUpdateReconciliationEnabledErrorComponent
        | ApiV1CertificatesPartialUpdateRenewalTimeErrorComponent
        | ApiV1CertificatesPartialUpdateSecretNameErrorComponent
        | ApiV1CertificatesPartialUpdateSlaAvailabilityErrorComponent
        | ApiV1CertificatesPartialUpdateSlaTargetErrorComponent
        | ApiV1CertificatesPartialUpdateSloAvailabilityErrorComponent
        | ApiV1CertificatesPartialUpdateSloTargetErrorComponent
        | ApiV1CertificatesPartialUpdateTargetAvailabilityErrorComponent
        | ApiV1CertificatesPartialUpdateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_certificates_partial_update_annotations_error_component import (
            ApiV1CertificatesPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_archived_at_error_component import (
            ApiV1CertificatesPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_archived_error_component import (
            ApiV1CertificatesPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_archived_reason_error_component import (
            ApiV1CertificatesPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_cert_manager_status_error_component import (
            ApiV1CertificatesPartialUpdateCertManagerStatusErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_certificate_status_error_component import (
            ApiV1CertificatesPartialUpdateCertificateStatusErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_challenge_reason_error_component import (
            ApiV1CertificatesPartialUpdateChallengeReasonErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_criticality_error_component import (
            ApiV1CertificatesPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_current_challenge_status_error_component import (
            ApiV1CertificatesPartialUpdateCurrentChallengeStatusErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_current_challenge_type_error_component import (
            ApiV1CertificatesPartialUpdateCurrentChallengeTypeErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_debug_mode_error_component import (
            ApiV1CertificatesPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_display_name_error_component import (
            ApiV1CertificatesPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_dns_names_error_component import (
            ApiV1CertificatesPartialUpdateDnsNamesErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_failure_reason_error_component import (
            ApiV1CertificatesPartialUpdateFailureReasonErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_ip_addresses_error_component import (
            ApiV1CertificatesPartialUpdateIpAddressesErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_is_ready_error_component import (
            ApiV1CertificatesPartialUpdateIsReadyErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_issuer_group_error_component import (
            ApiV1CertificatesPartialUpdateIssuerGroupErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_issuer_kind_error_component import (
            ApiV1CertificatesPartialUpdateIssuerKindErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_issuer_name_error_component import (
            ApiV1CertificatesPartialUpdateIssuerNameErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_k8s_cluster_error_component import (
            ApiV1CertificatesPartialUpdateK8SClusterErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_kind_error_component import (
            ApiV1CertificatesPartialUpdateKindErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_labels_error_component import (
            ApiV1CertificatesPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_last_failure_time_error_component import (
            ApiV1CertificatesPartialUpdateLastFailureTimeErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_last_synced_from_cluster_error_component import (
            ApiV1CertificatesPartialUpdateLastSyncedFromClusterErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_name_error_component import (
            ApiV1CertificatesPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_namespace_error_component import (
            ApiV1CertificatesPartialUpdateNamespaceErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_non_field_errors_error_component import (
            ApiV1CertificatesPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_not_after_error_component import (
            ApiV1CertificatesPartialUpdateNotAfterErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_not_before_error_component import (
            ApiV1CertificatesPartialUpdateNotBeforeErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_platform_service_error_component import (
            ApiV1CertificatesPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_provider_error_component import (
            ApiV1CertificatesPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_provider_id_error_component import (
            ApiV1CertificatesPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_provider_reference_error_component import (
            ApiV1CertificatesPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_reconciliation_enabled_error_component import (
            ApiV1CertificatesPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_renewal_time_error_component import (
            ApiV1CertificatesPartialUpdateRenewalTimeErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_secret_name_error_component import (
            ApiV1CertificatesPartialUpdateSecretNameErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_sla_availability_error_component import (
            ApiV1CertificatesPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_sla_target_error_component import (
            ApiV1CertificatesPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_slo_availability_error_component import (
            ApiV1CertificatesPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_slo_target_error_component import (
            ApiV1CertificatesPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_target_availability_error_component import (
            ApiV1CertificatesPartialUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_tolerations_error_component import (
            ApiV1CertificatesPartialUpdateTolerationsErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1CertificatesPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesPartialUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesPartialUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesPartialUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesPartialUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesPartialUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesPartialUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesPartialUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesPartialUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesPartialUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesPartialUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesPartialUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesPartialUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesPartialUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesPartialUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesPartialUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesPartialUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesPartialUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesPartialUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesPartialUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesPartialUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesPartialUpdateSecretNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesPartialUpdateNamespaceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesPartialUpdateDnsNamesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesPartialUpdateIpAddressesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesPartialUpdateIssuerNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesPartialUpdateIssuerKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesPartialUpdateIssuerGroupErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesPartialUpdateNotBeforeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesPartialUpdateNotAfterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesPartialUpdateRenewalTimeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesPartialUpdateCertificateStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesPartialUpdateIsReadyErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesPartialUpdateCurrentChallengeTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesPartialUpdateCurrentChallengeStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesPartialUpdateChallengeReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesPartialUpdateLastFailureTimeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesPartialUpdateFailureReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesPartialUpdateLastSyncedFromClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesPartialUpdateCertManagerStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesPartialUpdateK8SClusterErrorComponent):
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
        from ..models.api_v1_certificates_partial_update_annotations_error_component import (
            ApiV1CertificatesPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_archived_at_error_component import (
            ApiV1CertificatesPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_archived_error_component import (
            ApiV1CertificatesPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_archived_reason_error_component import (
            ApiV1CertificatesPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_cert_manager_status_error_component import (
            ApiV1CertificatesPartialUpdateCertManagerStatusErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_certificate_status_error_component import (
            ApiV1CertificatesPartialUpdateCertificateStatusErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_challenge_reason_error_component import (
            ApiV1CertificatesPartialUpdateChallengeReasonErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_criticality_error_component import (
            ApiV1CertificatesPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_current_challenge_status_error_component import (
            ApiV1CertificatesPartialUpdateCurrentChallengeStatusErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_current_challenge_type_error_component import (
            ApiV1CertificatesPartialUpdateCurrentChallengeTypeErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_debug_mode_error_component import (
            ApiV1CertificatesPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_display_name_error_component import (
            ApiV1CertificatesPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_dns_names_error_component import (
            ApiV1CertificatesPartialUpdateDnsNamesErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_failure_reason_error_component import (
            ApiV1CertificatesPartialUpdateFailureReasonErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_ip_addresses_error_component import (
            ApiV1CertificatesPartialUpdateIpAddressesErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_is_ready_error_component import (
            ApiV1CertificatesPartialUpdateIsReadyErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_issuer_group_error_component import (
            ApiV1CertificatesPartialUpdateIssuerGroupErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_issuer_kind_error_component import (
            ApiV1CertificatesPartialUpdateIssuerKindErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_issuer_name_error_component import (
            ApiV1CertificatesPartialUpdateIssuerNameErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_k8s_cluster_error_component import (
            ApiV1CertificatesPartialUpdateK8SClusterErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_kind_error_component import (
            ApiV1CertificatesPartialUpdateKindErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_labels_error_component import (
            ApiV1CertificatesPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_last_failure_time_error_component import (
            ApiV1CertificatesPartialUpdateLastFailureTimeErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_last_synced_from_cluster_error_component import (
            ApiV1CertificatesPartialUpdateLastSyncedFromClusterErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_metadata_error_component import (
            ApiV1CertificatesPartialUpdateMetadataErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_name_error_component import (
            ApiV1CertificatesPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_namespace_error_component import (
            ApiV1CertificatesPartialUpdateNamespaceErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_non_field_errors_error_component import (
            ApiV1CertificatesPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_not_after_error_component import (
            ApiV1CertificatesPartialUpdateNotAfterErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_not_before_error_component import (
            ApiV1CertificatesPartialUpdateNotBeforeErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_platform_service_error_component import (
            ApiV1CertificatesPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_provider_error_component import (
            ApiV1CertificatesPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_provider_id_error_component import (
            ApiV1CertificatesPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_provider_reference_error_component import (
            ApiV1CertificatesPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_reconciliation_enabled_error_component import (
            ApiV1CertificatesPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_renewal_time_error_component import (
            ApiV1CertificatesPartialUpdateRenewalTimeErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_secret_name_error_component import (
            ApiV1CertificatesPartialUpdateSecretNameErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_sla_availability_error_component import (
            ApiV1CertificatesPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_sla_target_error_component import (
            ApiV1CertificatesPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_slo_availability_error_component import (
            ApiV1CertificatesPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_slo_target_error_component import (
            ApiV1CertificatesPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_target_availability_error_component import (
            ApiV1CertificatesPartialUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_certificates_partial_update_tolerations_error_component import (
            ApiV1CertificatesPartialUpdateTolerationsErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1CertificatesPartialUpdateAnnotationsErrorComponent
                | ApiV1CertificatesPartialUpdateArchivedAtErrorComponent
                | ApiV1CertificatesPartialUpdateArchivedErrorComponent
                | ApiV1CertificatesPartialUpdateArchivedReasonErrorComponent
                | ApiV1CertificatesPartialUpdateCertificateStatusErrorComponent
                | ApiV1CertificatesPartialUpdateCertManagerStatusErrorComponent
                | ApiV1CertificatesPartialUpdateChallengeReasonErrorComponent
                | ApiV1CertificatesPartialUpdateCriticalityErrorComponent
                | ApiV1CertificatesPartialUpdateCurrentChallengeStatusErrorComponent
                | ApiV1CertificatesPartialUpdateCurrentChallengeTypeErrorComponent
                | ApiV1CertificatesPartialUpdateDebugModeErrorComponent
                | ApiV1CertificatesPartialUpdateDisplayNameErrorComponent
                | ApiV1CertificatesPartialUpdateDnsNamesErrorComponent
                | ApiV1CertificatesPartialUpdateFailureReasonErrorComponent
                | ApiV1CertificatesPartialUpdateIpAddressesErrorComponent
                | ApiV1CertificatesPartialUpdateIsReadyErrorComponent
                | ApiV1CertificatesPartialUpdateIssuerGroupErrorComponent
                | ApiV1CertificatesPartialUpdateIssuerKindErrorComponent
                | ApiV1CertificatesPartialUpdateIssuerNameErrorComponent
                | ApiV1CertificatesPartialUpdateK8SClusterErrorComponent
                | ApiV1CertificatesPartialUpdateKindErrorComponent
                | ApiV1CertificatesPartialUpdateLabelsErrorComponent
                | ApiV1CertificatesPartialUpdateLastFailureTimeErrorComponent
                | ApiV1CertificatesPartialUpdateLastSyncedFromClusterErrorComponent
                | ApiV1CertificatesPartialUpdateMetadataErrorComponent
                | ApiV1CertificatesPartialUpdateNameErrorComponent
                | ApiV1CertificatesPartialUpdateNamespaceErrorComponent
                | ApiV1CertificatesPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1CertificatesPartialUpdateNotAfterErrorComponent
                | ApiV1CertificatesPartialUpdateNotBeforeErrorComponent
                | ApiV1CertificatesPartialUpdatePlatformServiceErrorComponent
                | ApiV1CertificatesPartialUpdateProviderErrorComponent
                | ApiV1CertificatesPartialUpdateProviderIdErrorComponent
                | ApiV1CertificatesPartialUpdateProviderReferenceErrorComponent
                | ApiV1CertificatesPartialUpdateReconciliationEnabledErrorComponent
                | ApiV1CertificatesPartialUpdateRenewalTimeErrorComponent
                | ApiV1CertificatesPartialUpdateSecretNameErrorComponent
                | ApiV1CertificatesPartialUpdateSlaAvailabilityErrorComponent
                | ApiV1CertificatesPartialUpdateSlaTargetErrorComponent
                | ApiV1CertificatesPartialUpdateSloAvailabilityErrorComponent
                | ApiV1CertificatesPartialUpdateSloTargetErrorComponent
                | ApiV1CertificatesPartialUpdateTargetAvailabilityErrorComponent
                | ApiV1CertificatesPartialUpdateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_partial_update_error_type_0 = (
                        ApiV1CertificatesPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_partial_update_error_type_1 = (
                        ApiV1CertificatesPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_partial_update_error_type_2 = (
                        ApiV1CertificatesPartialUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_partial_update_error_type_3 = (
                        ApiV1CertificatesPartialUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_partial_update_error_type_4 = (
                        ApiV1CertificatesPartialUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_partial_update_error_type_5 = (
                        ApiV1CertificatesPartialUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_partial_update_error_type_6 = (
                        ApiV1CertificatesPartialUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_partial_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_partial_update_error_type_7 = (
                        ApiV1CertificatesPartialUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_partial_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_partial_update_error_type_8 = (
                        ApiV1CertificatesPartialUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_partial_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_partial_update_error_type_9 = (
                        ApiV1CertificatesPartialUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_partial_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_partial_update_error_type_10 = (
                        ApiV1CertificatesPartialUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_partial_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_partial_update_error_type_11 = (
                        ApiV1CertificatesPartialUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_partial_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_partial_update_error_type_12 = (
                        ApiV1CertificatesPartialUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_partial_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_partial_update_error_type_13 = (
                        ApiV1CertificatesPartialUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_partial_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_partial_update_error_type_14 = (
                        ApiV1CertificatesPartialUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_partial_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_partial_update_error_type_15 = (
                        ApiV1CertificatesPartialUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_partial_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_partial_update_error_type_16 = (
                        ApiV1CertificatesPartialUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_partial_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_partial_update_error_type_17 = (
                        ApiV1CertificatesPartialUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_partial_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_partial_update_error_type_18 = (
                        ApiV1CertificatesPartialUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_partial_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_partial_update_error_type_19 = (
                        ApiV1CertificatesPartialUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_partial_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_partial_update_error_type_20 = (
                        ApiV1CertificatesPartialUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_partial_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_partial_update_error_type_21 = (
                        ApiV1CertificatesPartialUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_partial_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_partial_update_error_type_22 = (
                        ApiV1CertificatesPartialUpdateSecretNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_partial_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_partial_update_error_type_23 = (
                        ApiV1CertificatesPartialUpdateNamespaceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_partial_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_partial_update_error_type_24 = (
                        ApiV1CertificatesPartialUpdateDnsNamesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_partial_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_partial_update_error_type_25 = (
                        ApiV1CertificatesPartialUpdateIpAddressesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_partial_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_partial_update_error_type_26 = (
                        ApiV1CertificatesPartialUpdateIssuerNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_partial_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_partial_update_error_type_27 = (
                        ApiV1CertificatesPartialUpdateIssuerKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_partial_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_partial_update_error_type_28 = (
                        ApiV1CertificatesPartialUpdateIssuerGroupErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_partial_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_partial_update_error_type_29 = (
                        ApiV1CertificatesPartialUpdateNotBeforeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_partial_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_partial_update_error_type_30 = (
                        ApiV1CertificatesPartialUpdateNotAfterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_partial_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_partial_update_error_type_31 = (
                        ApiV1CertificatesPartialUpdateRenewalTimeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_partial_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_partial_update_error_type_32 = (
                        ApiV1CertificatesPartialUpdateCertificateStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_partial_update_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_partial_update_error_type_33 = (
                        ApiV1CertificatesPartialUpdateIsReadyErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_partial_update_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_partial_update_error_type_34 = (
                        ApiV1CertificatesPartialUpdateCurrentChallengeTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_partial_update_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_partial_update_error_type_35 = (
                        ApiV1CertificatesPartialUpdateCurrentChallengeStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_partial_update_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_partial_update_error_type_36 = (
                        ApiV1CertificatesPartialUpdateChallengeReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_partial_update_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_partial_update_error_type_37 = (
                        ApiV1CertificatesPartialUpdateLastFailureTimeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_partial_update_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_partial_update_error_type_38 = (
                        ApiV1CertificatesPartialUpdateFailureReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_partial_update_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_partial_update_error_type_39 = (
                        ApiV1CertificatesPartialUpdateLastSyncedFromClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_partial_update_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_partial_update_error_type_40 = (
                        ApiV1CertificatesPartialUpdateCertManagerStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_partial_update_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_partial_update_error_type_41 = (
                        ApiV1CertificatesPartialUpdateK8SClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_partial_update_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_certificates_partial_update_error_type_42 = (
                    ApiV1CertificatesPartialUpdateMetadataErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_certificates_partial_update_error_type_42

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_certificates_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_certificates_partial_update_validation_error.additional_properties = d
        return api_v1_certificates_partial_update_validation_error

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
