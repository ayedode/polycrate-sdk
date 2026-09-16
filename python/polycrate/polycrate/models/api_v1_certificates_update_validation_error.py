from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_certificates_update_annotations_error_component import (
        ApiV1CertificatesUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_certificates_update_archived_at_error_component import (
        ApiV1CertificatesUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_certificates_update_archived_error_component import (
        ApiV1CertificatesUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_certificates_update_archived_reason_error_component import (
        ApiV1CertificatesUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_certificates_update_cert_manager_status_error_component import (
        ApiV1CertificatesUpdateCertManagerStatusErrorComponent,
    )
    from ..models.api_v1_certificates_update_certificate_status_error_component import (
        ApiV1CertificatesUpdateCertificateStatusErrorComponent,
    )
    from ..models.api_v1_certificates_update_challenge_reason_error_component import (
        ApiV1CertificatesUpdateChallengeReasonErrorComponent,
    )
    from ..models.api_v1_certificates_update_criticality_error_component import (
        ApiV1CertificatesUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_certificates_update_current_challenge_status_error_component import (
        ApiV1CertificatesUpdateCurrentChallengeStatusErrorComponent,
    )
    from ..models.api_v1_certificates_update_current_challenge_type_error_component import (
        ApiV1CertificatesUpdateCurrentChallengeTypeErrorComponent,
    )
    from ..models.api_v1_certificates_update_debug_mode_error_component import (
        ApiV1CertificatesUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_certificates_update_display_name_error_component import (
        ApiV1CertificatesUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_certificates_update_dns_names_error_component import (
        ApiV1CertificatesUpdateDnsNamesErrorComponent,
    )
    from ..models.api_v1_certificates_update_failure_reason_error_component import (
        ApiV1CertificatesUpdateFailureReasonErrorComponent,
    )
    from ..models.api_v1_certificates_update_ip_addresses_error_component import (
        ApiV1CertificatesUpdateIpAddressesErrorComponent,
    )
    from ..models.api_v1_certificates_update_is_ready_error_component import (
        ApiV1CertificatesUpdateIsReadyErrorComponent,
    )
    from ..models.api_v1_certificates_update_issuer_group_error_component import (
        ApiV1CertificatesUpdateIssuerGroupErrorComponent,
    )
    from ..models.api_v1_certificates_update_issuer_kind_error_component import (
        ApiV1CertificatesUpdateIssuerKindErrorComponent,
    )
    from ..models.api_v1_certificates_update_issuer_name_error_component import (
        ApiV1CertificatesUpdateIssuerNameErrorComponent,
    )
    from ..models.api_v1_certificates_update_k8s_cluster_error_component import (
        ApiV1CertificatesUpdateK8SClusterErrorComponent,
    )
    from ..models.api_v1_certificates_update_kind_error_component import ApiV1CertificatesUpdateKindErrorComponent
    from ..models.api_v1_certificates_update_labels_error_component import ApiV1CertificatesUpdateLabelsErrorComponent
    from ..models.api_v1_certificates_update_last_failure_time_error_component import (
        ApiV1CertificatesUpdateLastFailureTimeErrorComponent,
    )
    from ..models.api_v1_certificates_update_last_synced_from_cluster_error_component import (
        ApiV1CertificatesUpdateLastSyncedFromClusterErrorComponent,
    )
    from ..models.api_v1_certificates_update_metadata_error_component import (
        ApiV1CertificatesUpdateMetadataErrorComponent,
    )
    from ..models.api_v1_certificates_update_name_error_component import ApiV1CertificatesUpdateNameErrorComponent
    from ..models.api_v1_certificates_update_namespace_error_component import (
        ApiV1CertificatesUpdateNamespaceErrorComponent,
    )
    from ..models.api_v1_certificates_update_non_field_errors_error_component import (
        ApiV1CertificatesUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_certificates_update_not_after_error_component import (
        ApiV1CertificatesUpdateNotAfterErrorComponent,
    )
    from ..models.api_v1_certificates_update_not_before_error_component import (
        ApiV1CertificatesUpdateNotBeforeErrorComponent,
    )
    from ..models.api_v1_certificates_update_platform_service_error_component import (
        ApiV1CertificatesUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_certificates_update_provider_error_component import (
        ApiV1CertificatesUpdateProviderErrorComponent,
    )
    from ..models.api_v1_certificates_update_provider_id_error_component import (
        ApiV1CertificatesUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_certificates_update_provider_reference_error_component import (
        ApiV1CertificatesUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_certificates_update_reconciliation_enabled_error_component import (
        ApiV1CertificatesUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_certificates_update_renewal_time_error_component import (
        ApiV1CertificatesUpdateRenewalTimeErrorComponent,
    )
    from ..models.api_v1_certificates_update_secret_name_error_component import (
        ApiV1CertificatesUpdateSecretNameErrorComponent,
    )
    from ..models.api_v1_certificates_update_sla_availability_error_component import (
        ApiV1CertificatesUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_certificates_update_sla_target_error_component import (
        ApiV1CertificatesUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_certificates_update_slo_availability_error_component import (
        ApiV1CertificatesUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_certificates_update_slo_target_error_component import (
        ApiV1CertificatesUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_certificates_update_target_availability_error_component import (
        ApiV1CertificatesUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_certificates_update_tolerations_error_component import (
        ApiV1CertificatesUpdateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1CertificatesUpdateValidationError")


@_attrs_define
class ApiV1CertificatesUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1CertificatesUpdateAnnotationsErrorComponent | ApiV1CertificatesUpdateArchivedAtErrorComponent
            | ApiV1CertificatesUpdateArchivedErrorComponent | ApiV1CertificatesUpdateArchivedReasonErrorComponent |
            ApiV1CertificatesUpdateCertificateStatusErrorComponent | ApiV1CertificatesUpdateCertManagerStatusErrorComponent
            | ApiV1CertificatesUpdateChallengeReasonErrorComponent | ApiV1CertificatesUpdateCriticalityErrorComponent |
            ApiV1CertificatesUpdateCurrentChallengeStatusErrorComponent |
            ApiV1CertificatesUpdateCurrentChallengeTypeErrorComponent | ApiV1CertificatesUpdateDebugModeErrorComponent |
            ApiV1CertificatesUpdateDisplayNameErrorComponent | ApiV1CertificatesUpdateDnsNamesErrorComponent |
            ApiV1CertificatesUpdateFailureReasonErrorComponent | ApiV1CertificatesUpdateIpAddressesErrorComponent |
            ApiV1CertificatesUpdateIsReadyErrorComponent | ApiV1CertificatesUpdateIssuerGroupErrorComponent |
            ApiV1CertificatesUpdateIssuerKindErrorComponent | ApiV1CertificatesUpdateIssuerNameErrorComponent |
            ApiV1CertificatesUpdateK8SClusterErrorComponent | ApiV1CertificatesUpdateKindErrorComponent |
            ApiV1CertificatesUpdateLabelsErrorComponent | ApiV1CertificatesUpdateLastFailureTimeErrorComponent |
            ApiV1CertificatesUpdateLastSyncedFromClusterErrorComponent | ApiV1CertificatesUpdateMetadataErrorComponent |
            ApiV1CertificatesUpdateNameErrorComponent | ApiV1CertificatesUpdateNamespaceErrorComponent |
            ApiV1CertificatesUpdateNonFieldErrorsErrorComponent | ApiV1CertificatesUpdateNotAfterErrorComponent |
            ApiV1CertificatesUpdateNotBeforeErrorComponent | ApiV1CertificatesUpdatePlatformServiceErrorComponent |
            ApiV1CertificatesUpdateProviderErrorComponent | ApiV1CertificatesUpdateProviderIdErrorComponent |
            ApiV1CertificatesUpdateProviderReferenceErrorComponent |
            ApiV1CertificatesUpdateReconciliationEnabledErrorComponent | ApiV1CertificatesUpdateRenewalTimeErrorComponent |
            ApiV1CertificatesUpdateSecretNameErrorComponent | ApiV1CertificatesUpdateSlaAvailabilityErrorComponent |
            ApiV1CertificatesUpdateSlaTargetErrorComponent | ApiV1CertificatesUpdateSloAvailabilityErrorComponent |
            ApiV1CertificatesUpdateSloTargetErrorComponent | ApiV1CertificatesUpdateTargetAvailabilityErrorComponent |
            ApiV1CertificatesUpdateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1CertificatesUpdateAnnotationsErrorComponent
        | ApiV1CertificatesUpdateArchivedAtErrorComponent
        | ApiV1CertificatesUpdateArchivedErrorComponent
        | ApiV1CertificatesUpdateArchivedReasonErrorComponent
        | ApiV1CertificatesUpdateCertificateStatusErrorComponent
        | ApiV1CertificatesUpdateCertManagerStatusErrorComponent
        | ApiV1CertificatesUpdateChallengeReasonErrorComponent
        | ApiV1CertificatesUpdateCriticalityErrorComponent
        | ApiV1CertificatesUpdateCurrentChallengeStatusErrorComponent
        | ApiV1CertificatesUpdateCurrentChallengeTypeErrorComponent
        | ApiV1CertificatesUpdateDebugModeErrorComponent
        | ApiV1CertificatesUpdateDisplayNameErrorComponent
        | ApiV1CertificatesUpdateDnsNamesErrorComponent
        | ApiV1CertificatesUpdateFailureReasonErrorComponent
        | ApiV1CertificatesUpdateIpAddressesErrorComponent
        | ApiV1CertificatesUpdateIsReadyErrorComponent
        | ApiV1CertificatesUpdateIssuerGroupErrorComponent
        | ApiV1CertificatesUpdateIssuerKindErrorComponent
        | ApiV1CertificatesUpdateIssuerNameErrorComponent
        | ApiV1CertificatesUpdateK8SClusterErrorComponent
        | ApiV1CertificatesUpdateKindErrorComponent
        | ApiV1CertificatesUpdateLabelsErrorComponent
        | ApiV1CertificatesUpdateLastFailureTimeErrorComponent
        | ApiV1CertificatesUpdateLastSyncedFromClusterErrorComponent
        | ApiV1CertificatesUpdateMetadataErrorComponent
        | ApiV1CertificatesUpdateNameErrorComponent
        | ApiV1CertificatesUpdateNamespaceErrorComponent
        | ApiV1CertificatesUpdateNonFieldErrorsErrorComponent
        | ApiV1CertificatesUpdateNotAfterErrorComponent
        | ApiV1CertificatesUpdateNotBeforeErrorComponent
        | ApiV1CertificatesUpdatePlatformServiceErrorComponent
        | ApiV1CertificatesUpdateProviderErrorComponent
        | ApiV1CertificatesUpdateProviderIdErrorComponent
        | ApiV1CertificatesUpdateProviderReferenceErrorComponent
        | ApiV1CertificatesUpdateReconciliationEnabledErrorComponent
        | ApiV1CertificatesUpdateRenewalTimeErrorComponent
        | ApiV1CertificatesUpdateSecretNameErrorComponent
        | ApiV1CertificatesUpdateSlaAvailabilityErrorComponent
        | ApiV1CertificatesUpdateSlaTargetErrorComponent
        | ApiV1CertificatesUpdateSloAvailabilityErrorComponent
        | ApiV1CertificatesUpdateSloTargetErrorComponent
        | ApiV1CertificatesUpdateTargetAvailabilityErrorComponent
        | ApiV1CertificatesUpdateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_certificates_update_annotations_error_component import (
            ApiV1CertificatesUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_archived_at_error_component import (
            ApiV1CertificatesUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_archived_error_component import (
            ApiV1CertificatesUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_archived_reason_error_component import (
            ApiV1CertificatesUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_cert_manager_status_error_component import (
            ApiV1CertificatesUpdateCertManagerStatusErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_certificate_status_error_component import (
            ApiV1CertificatesUpdateCertificateStatusErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_challenge_reason_error_component import (
            ApiV1CertificatesUpdateChallengeReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_criticality_error_component import (
            ApiV1CertificatesUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_current_challenge_status_error_component import (
            ApiV1CertificatesUpdateCurrentChallengeStatusErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_current_challenge_type_error_component import (
            ApiV1CertificatesUpdateCurrentChallengeTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_debug_mode_error_component import (
            ApiV1CertificatesUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_display_name_error_component import (
            ApiV1CertificatesUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_dns_names_error_component import (
            ApiV1CertificatesUpdateDnsNamesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_failure_reason_error_component import (
            ApiV1CertificatesUpdateFailureReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_ip_addresses_error_component import (
            ApiV1CertificatesUpdateIpAddressesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_is_ready_error_component import (
            ApiV1CertificatesUpdateIsReadyErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_issuer_group_error_component import (
            ApiV1CertificatesUpdateIssuerGroupErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_issuer_kind_error_component import (
            ApiV1CertificatesUpdateIssuerKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_issuer_name_error_component import (
            ApiV1CertificatesUpdateIssuerNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_k8s_cluster_error_component import (
            ApiV1CertificatesUpdateK8SClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_kind_error_component import (
            ApiV1CertificatesUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_labels_error_component import (
            ApiV1CertificatesUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_last_failure_time_error_component import (
            ApiV1CertificatesUpdateLastFailureTimeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_last_synced_from_cluster_error_component import (
            ApiV1CertificatesUpdateLastSyncedFromClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_name_error_component import (
            ApiV1CertificatesUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_namespace_error_component import (
            ApiV1CertificatesUpdateNamespaceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_non_field_errors_error_component import (
            ApiV1CertificatesUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_not_after_error_component import (
            ApiV1CertificatesUpdateNotAfterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_not_before_error_component import (
            ApiV1CertificatesUpdateNotBeforeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_platform_service_error_component import (
            ApiV1CertificatesUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_provider_error_component import (
            ApiV1CertificatesUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_provider_id_error_component import (
            ApiV1CertificatesUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_provider_reference_error_component import (
            ApiV1CertificatesUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_reconciliation_enabled_error_component import (
            ApiV1CertificatesUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_renewal_time_error_component import (
            ApiV1CertificatesUpdateRenewalTimeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_secret_name_error_component import (
            ApiV1CertificatesUpdateSecretNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_sla_availability_error_component import (
            ApiV1CertificatesUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_sla_target_error_component import (
            ApiV1CertificatesUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_slo_availability_error_component import (
            ApiV1CertificatesUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_slo_target_error_component import (
            ApiV1CertificatesUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_target_availability_error_component import (
            ApiV1CertificatesUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_tolerations_error_component import (
            ApiV1CertificatesUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1CertificatesUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesUpdateSecretNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesUpdateNamespaceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesUpdateDnsNamesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesUpdateIpAddressesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesUpdateIssuerNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesUpdateIssuerKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesUpdateIssuerGroupErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesUpdateNotBeforeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesUpdateNotAfterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesUpdateRenewalTimeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesUpdateCertificateStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesUpdateIsReadyErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesUpdateCurrentChallengeTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesUpdateCurrentChallengeStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesUpdateChallengeReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesUpdateLastFailureTimeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesUpdateFailureReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesUpdateLastSyncedFromClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesUpdateCertManagerStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesUpdateK8SClusterErrorComponent):
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
        from ..models.api_v1_certificates_update_annotations_error_component import (
            ApiV1CertificatesUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_archived_at_error_component import (
            ApiV1CertificatesUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_archived_error_component import (
            ApiV1CertificatesUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_archived_reason_error_component import (
            ApiV1CertificatesUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_cert_manager_status_error_component import (
            ApiV1CertificatesUpdateCertManagerStatusErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_certificate_status_error_component import (
            ApiV1CertificatesUpdateCertificateStatusErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_challenge_reason_error_component import (
            ApiV1CertificatesUpdateChallengeReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_criticality_error_component import (
            ApiV1CertificatesUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_current_challenge_status_error_component import (
            ApiV1CertificatesUpdateCurrentChallengeStatusErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_current_challenge_type_error_component import (
            ApiV1CertificatesUpdateCurrentChallengeTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_debug_mode_error_component import (
            ApiV1CertificatesUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_display_name_error_component import (
            ApiV1CertificatesUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_dns_names_error_component import (
            ApiV1CertificatesUpdateDnsNamesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_failure_reason_error_component import (
            ApiV1CertificatesUpdateFailureReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_ip_addresses_error_component import (
            ApiV1CertificatesUpdateIpAddressesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_is_ready_error_component import (
            ApiV1CertificatesUpdateIsReadyErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_issuer_group_error_component import (
            ApiV1CertificatesUpdateIssuerGroupErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_issuer_kind_error_component import (
            ApiV1CertificatesUpdateIssuerKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_issuer_name_error_component import (
            ApiV1CertificatesUpdateIssuerNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_k8s_cluster_error_component import (
            ApiV1CertificatesUpdateK8SClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_kind_error_component import (
            ApiV1CertificatesUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_labels_error_component import (
            ApiV1CertificatesUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_last_failure_time_error_component import (
            ApiV1CertificatesUpdateLastFailureTimeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_last_synced_from_cluster_error_component import (
            ApiV1CertificatesUpdateLastSyncedFromClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_metadata_error_component import (
            ApiV1CertificatesUpdateMetadataErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_name_error_component import (
            ApiV1CertificatesUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_namespace_error_component import (
            ApiV1CertificatesUpdateNamespaceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_non_field_errors_error_component import (
            ApiV1CertificatesUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_not_after_error_component import (
            ApiV1CertificatesUpdateNotAfterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_not_before_error_component import (
            ApiV1CertificatesUpdateNotBeforeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_platform_service_error_component import (
            ApiV1CertificatesUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_provider_error_component import (
            ApiV1CertificatesUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_provider_id_error_component import (
            ApiV1CertificatesUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_provider_reference_error_component import (
            ApiV1CertificatesUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_reconciliation_enabled_error_component import (
            ApiV1CertificatesUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_renewal_time_error_component import (
            ApiV1CertificatesUpdateRenewalTimeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_secret_name_error_component import (
            ApiV1CertificatesUpdateSecretNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_sla_availability_error_component import (
            ApiV1CertificatesUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_sla_target_error_component import (
            ApiV1CertificatesUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_slo_availability_error_component import (
            ApiV1CertificatesUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_slo_target_error_component import (
            ApiV1CertificatesUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_target_availability_error_component import (
            ApiV1CertificatesUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_update_tolerations_error_component import (
            ApiV1CertificatesUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1CertificatesUpdateAnnotationsErrorComponent
                | ApiV1CertificatesUpdateArchivedAtErrorComponent
                | ApiV1CertificatesUpdateArchivedErrorComponent
                | ApiV1CertificatesUpdateArchivedReasonErrorComponent
                | ApiV1CertificatesUpdateCertificateStatusErrorComponent
                | ApiV1CertificatesUpdateCertManagerStatusErrorComponent
                | ApiV1CertificatesUpdateChallengeReasonErrorComponent
                | ApiV1CertificatesUpdateCriticalityErrorComponent
                | ApiV1CertificatesUpdateCurrentChallengeStatusErrorComponent
                | ApiV1CertificatesUpdateCurrentChallengeTypeErrorComponent
                | ApiV1CertificatesUpdateDebugModeErrorComponent
                | ApiV1CertificatesUpdateDisplayNameErrorComponent
                | ApiV1CertificatesUpdateDnsNamesErrorComponent
                | ApiV1CertificatesUpdateFailureReasonErrorComponent
                | ApiV1CertificatesUpdateIpAddressesErrorComponent
                | ApiV1CertificatesUpdateIsReadyErrorComponent
                | ApiV1CertificatesUpdateIssuerGroupErrorComponent
                | ApiV1CertificatesUpdateIssuerKindErrorComponent
                | ApiV1CertificatesUpdateIssuerNameErrorComponent
                | ApiV1CertificatesUpdateK8SClusterErrorComponent
                | ApiV1CertificatesUpdateKindErrorComponent
                | ApiV1CertificatesUpdateLabelsErrorComponent
                | ApiV1CertificatesUpdateLastFailureTimeErrorComponent
                | ApiV1CertificatesUpdateLastSyncedFromClusterErrorComponent
                | ApiV1CertificatesUpdateMetadataErrorComponent
                | ApiV1CertificatesUpdateNameErrorComponent
                | ApiV1CertificatesUpdateNamespaceErrorComponent
                | ApiV1CertificatesUpdateNonFieldErrorsErrorComponent
                | ApiV1CertificatesUpdateNotAfterErrorComponent
                | ApiV1CertificatesUpdateNotBeforeErrorComponent
                | ApiV1CertificatesUpdatePlatformServiceErrorComponent
                | ApiV1CertificatesUpdateProviderErrorComponent
                | ApiV1CertificatesUpdateProviderIdErrorComponent
                | ApiV1CertificatesUpdateProviderReferenceErrorComponent
                | ApiV1CertificatesUpdateReconciliationEnabledErrorComponent
                | ApiV1CertificatesUpdateRenewalTimeErrorComponent
                | ApiV1CertificatesUpdateSecretNameErrorComponent
                | ApiV1CertificatesUpdateSlaAvailabilityErrorComponent
                | ApiV1CertificatesUpdateSlaTargetErrorComponent
                | ApiV1CertificatesUpdateSloAvailabilityErrorComponent
                | ApiV1CertificatesUpdateSloTargetErrorComponent
                | ApiV1CertificatesUpdateTargetAvailabilityErrorComponent
                | ApiV1CertificatesUpdateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_update_error_type_0 = (
                        ApiV1CertificatesUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_update_error_type_1 = (
                        ApiV1CertificatesUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_update_error_type_2 = (
                        ApiV1CertificatesUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_update_error_type_3 = (
                        ApiV1CertificatesUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_update_error_type_4 = (
                        ApiV1CertificatesUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_update_error_type_5 = (
                        ApiV1CertificatesUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_update_error_type_6 = (
                        ApiV1CertificatesUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_update_error_type_7 = (
                        ApiV1CertificatesUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_update_error_type_8 = (
                        ApiV1CertificatesUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_update_error_type_9 = (
                        ApiV1CertificatesUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_update_error_type_10 = (
                        ApiV1CertificatesUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_update_error_type_11 = (
                        ApiV1CertificatesUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_update_error_type_12 = (
                        ApiV1CertificatesUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_update_error_type_13 = (
                        ApiV1CertificatesUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_update_error_type_14 = (
                        ApiV1CertificatesUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_update_error_type_15 = (
                        ApiV1CertificatesUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_update_error_type_16 = (
                        ApiV1CertificatesUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_update_error_type_17 = (
                        ApiV1CertificatesUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_update_error_type_18 = (
                        ApiV1CertificatesUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_update_error_type_19 = (
                        ApiV1CertificatesUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_update_error_type_20 = (
                        ApiV1CertificatesUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_update_error_type_21 = (
                        ApiV1CertificatesUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_update_error_type_22 = (
                        ApiV1CertificatesUpdateSecretNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_update_error_type_23 = (
                        ApiV1CertificatesUpdateNamespaceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_update_error_type_24 = (
                        ApiV1CertificatesUpdateDnsNamesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_update_error_type_25 = (
                        ApiV1CertificatesUpdateIpAddressesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_update_error_type_26 = (
                        ApiV1CertificatesUpdateIssuerNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_update_error_type_27 = (
                        ApiV1CertificatesUpdateIssuerKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_update_error_type_28 = (
                        ApiV1CertificatesUpdateIssuerGroupErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_update_error_type_29 = (
                        ApiV1CertificatesUpdateNotBeforeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_update_error_type_30 = (
                        ApiV1CertificatesUpdateNotAfterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_update_error_type_31 = (
                        ApiV1CertificatesUpdateRenewalTimeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_update_error_type_32 = (
                        ApiV1CertificatesUpdateCertificateStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_update_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_update_error_type_33 = (
                        ApiV1CertificatesUpdateIsReadyErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_update_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_update_error_type_34 = (
                        ApiV1CertificatesUpdateCurrentChallengeTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_update_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_update_error_type_35 = (
                        ApiV1CertificatesUpdateCurrentChallengeStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_update_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_update_error_type_36 = (
                        ApiV1CertificatesUpdateChallengeReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_update_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_update_error_type_37 = (
                        ApiV1CertificatesUpdateLastFailureTimeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_update_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_update_error_type_38 = (
                        ApiV1CertificatesUpdateFailureReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_update_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_update_error_type_39 = (
                        ApiV1CertificatesUpdateLastSyncedFromClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_update_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_update_error_type_40 = (
                        ApiV1CertificatesUpdateCertManagerStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_update_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_update_error_type_41 = (
                        ApiV1CertificatesUpdateK8SClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_update_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_certificates_update_error_type_42 = (
                    ApiV1CertificatesUpdateMetadataErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_certificates_update_error_type_42

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_certificates_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_certificates_update_validation_error.additional_properties = d
        return api_v1_certificates_update_validation_error

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
