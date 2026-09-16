from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_certificates_archive_create_annotations_error_component import (
        ApiV1CertificatesArchiveCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_certificates_archive_create_archived_at_error_component import (
        ApiV1CertificatesArchiveCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_certificates_archive_create_archived_error_component import (
        ApiV1CertificatesArchiveCreateArchivedErrorComponent,
    )
    from ..models.api_v1_certificates_archive_create_archived_reason_error_component import (
        ApiV1CertificatesArchiveCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_certificates_archive_create_cert_manager_status_error_component import (
        ApiV1CertificatesArchiveCreateCertManagerStatusErrorComponent,
    )
    from ..models.api_v1_certificates_archive_create_certificate_status_error_component import (
        ApiV1CertificatesArchiveCreateCertificateStatusErrorComponent,
    )
    from ..models.api_v1_certificates_archive_create_challenge_reason_error_component import (
        ApiV1CertificatesArchiveCreateChallengeReasonErrorComponent,
    )
    from ..models.api_v1_certificates_archive_create_criticality_error_component import (
        ApiV1CertificatesArchiveCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_certificates_archive_create_current_challenge_status_error_component import (
        ApiV1CertificatesArchiveCreateCurrentChallengeStatusErrorComponent,
    )
    from ..models.api_v1_certificates_archive_create_current_challenge_type_error_component import (
        ApiV1CertificatesArchiveCreateCurrentChallengeTypeErrorComponent,
    )
    from ..models.api_v1_certificates_archive_create_debug_mode_error_component import (
        ApiV1CertificatesArchiveCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_certificates_archive_create_display_name_error_component import (
        ApiV1CertificatesArchiveCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_certificates_archive_create_dns_names_error_component import (
        ApiV1CertificatesArchiveCreateDnsNamesErrorComponent,
    )
    from ..models.api_v1_certificates_archive_create_failure_reason_error_component import (
        ApiV1CertificatesArchiveCreateFailureReasonErrorComponent,
    )
    from ..models.api_v1_certificates_archive_create_ip_addresses_error_component import (
        ApiV1CertificatesArchiveCreateIpAddressesErrorComponent,
    )
    from ..models.api_v1_certificates_archive_create_is_ready_error_component import (
        ApiV1CertificatesArchiveCreateIsReadyErrorComponent,
    )
    from ..models.api_v1_certificates_archive_create_issuer_group_error_component import (
        ApiV1CertificatesArchiveCreateIssuerGroupErrorComponent,
    )
    from ..models.api_v1_certificates_archive_create_issuer_kind_error_component import (
        ApiV1CertificatesArchiveCreateIssuerKindErrorComponent,
    )
    from ..models.api_v1_certificates_archive_create_issuer_name_error_component import (
        ApiV1CertificatesArchiveCreateIssuerNameErrorComponent,
    )
    from ..models.api_v1_certificates_archive_create_k8s_cluster_error_component import (
        ApiV1CertificatesArchiveCreateK8SClusterErrorComponent,
    )
    from ..models.api_v1_certificates_archive_create_kind_error_component import (
        ApiV1CertificatesArchiveCreateKindErrorComponent,
    )
    from ..models.api_v1_certificates_archive_create_labels_error_component import (
        ApiV1CertificatesArchiveCreateLabelsErrorComponent,
    )
    from ..models.api_v1_certificates_archive_create_last_failure_time_error_component import (
        ApiV1CertificatesArchiveCreateLastFailureTimeErrorComponent,
    )
    from ..models.api_v1_certificates_archive_create_last_synced_from_cluster_error_component import (
        ApiV1CertificatesArchiveCreateLastSyncedFromClusterErrorComponent,
    )
    from ..models.api_v1_certificates_archive_create_metadata_error_component import (
        ApiV1CertificatesArchiveCreateMetadataErrorComponent,
    )
    from ..models.api_v1_certificates_archive_create_name_error_component import (
        ApiV1CertificatesArchiveCreateNameErrorComponent,
    )
    from ..models.api_v1_certificates_archive_create_namespace_error_component import (
        ApiV1CertificatesArchiveCreateNamespaceErrorComponent,
    )
    from ..models.api_v1_certificates_archive_create_non_field_errors_error_component import (
        ApiV1CertificatesArchiveCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_certificates_archive_create_not_after_error_component import (
        ApiV1CertificatesArchiveCreateNotAfterErrorComponent,
    )
    from ..models.api_v1_certificates_archive_create_not_before_error_component import (
        ApiV1CertificatesArchiveCreateNotBeforeErrorComponent,
    )
    from ..models.api_v1_certificates_archive_create_platform_service_error_component import (
        ApiV1CertificatesArchiveCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_certificates_archive_create_provider_error_component import (
        ApiV1CertificatesArchiveCreateProviderErrorComponent,
    )
    from ..models.api_v1_certificates_archive_create_provider_id_error_component import (
        ApiV1CertificatesArchiveCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_certificates_archive_create_provider_reference_error_component import (
        ApiV1CertificatesArchiveCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_certificates_archive_create_reconciliation_enabled_error_component import (
        ApiV1CertificatesArchiveCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_certificates_archive_create_renewal_time_error_component import (
        ApiV1CertificatesArchiveCreateRenewalTimeErrorComponent,
    )
    from ..models.api_v1_certificates_archive_create_secret_name_error_component import (
        ApiV1CertificatesArchiveCreateSecretNameErrorComponent,
    )
    from ..models.api_v1_certificates_archive_create_sla_availability_error_component import (
        ApiV1CertificatesArchiveCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_certificates_archive_create_sla_target_error_component import (
        ApiV1CertificatesArchiveCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_certificates_archive_create_slo_availability_error_component import (
        ApiV1CertificatesArchiveCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_certificates_archive_create_slo_target_error_component import (
        ApiV1CertificatesArchiveCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_certificates_archive_create_target_availability_error_component import (
        ApiV1CertificatesArchiveCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_certificates_archive_create_tolerations_error_component import (
        ApiV1CertificatesArchiveCreateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1CertificatesArchiveCreateValidationError")


@_attrs_define
class ApiV1CertificatesArchiveCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1CertificatesArchiveCreateAnnotationsErrorComponent |
            ApiV1CertificatesArchiveCreateArchivedAtErrorComponent | ApiV1CertificatesArchiveCreateArchivedErrorComponent |
            ApiV1CertificatesArchiveCreateArchivedReasonErrorComponent |
            ApiV1CertificatesArchiveCreateCertificateStatusErrorComponent |
            ApiV1CertificatesArchiveCreateCertManagerStatusErrorComponent |
            ApiV1CertificatesArchiveCreateChallengeReasonErrorComponent |
            ApiV1CertificatesArchiveCreateCriticalityErrorComponent |
            ApiV1CertificatesArchiveCreateCurrentChallengeStatusErrorComponent |
            ApiV1CertificatesArchiveCreateCurrentChallengeTypeErrorComponent |
            ApiV1CertificatesArchiveCreateDebugModeErrorComponent | ApiV1CertificatesArchiveCreateDisplayNameErrorComponent
            | ApiV1CertificatesArchiveCreateDnsNamesErrorComponent |
            ApiV1CertificatesArchiveCreateFailureReasonErrorComponent |
            ApiV1CertificatesArchiveCreateIpAddressesErrorComponent | ApiV1CertificatesArchiveCreateIsReadyErrorComponent |
            ApiV1CertificatesArchiveCreateIssuerGroupErrorComponent | ApiV1CertificatesArchiveCreateIssuerKindErrorComponent
            | ApiV1CertificatesArchiveCreateIssuerNameErrorComponent |
            ApiV1CertificatesArchiveCreateK8SClusterErrorComponent | ApiV1CertificatesArchiveCreateKindErrorComponent |
            ApiV1CertificatesArchiveCreateLabelsErrorComponent | ApiV1CertificatesArchiveCreateLastFailureTimeErrorComponent
            | ApiV1CertificatesArchiveCreateLastSyncedFromClusterErrorComponent |
            ApiV1CertificatesArchiveCreateMetadataErrorComponent | ApiV1CertificatesArchiveCreateNameErrorComponent |
            ApiV1CertificatesArchiveCreateNamespaceErrorComponent |
            ApiV1CertificatesArchiveCreateNonFieldErrorsErrorComponent |
            ApiV1CertificatesArchiveCreateNotAfterErrorComponent | ApiV1CertificatesArchiveCreateNotBeforeErrorComponent |
            ApiV1CertificatesArchiveCreatePlatformServiceErrorComponent |
            ApiV1CertificatesArchiveCreateProviderErrorComponent | ApiV1CertificatesArchiveCreateProviderIdErrorComponent |
            ApiV1CertificatesArchiveCreateProviderReferenceErrorComponent |
            ApiV1CertificatesArchiveCreateReconciliationEnabledErrorComponent |
            ApiV1CertificatesArchiveCreateRenewalTimeErrorComponent | ApiV1CertificatesArchiveCreateSecretNameErrorComponent
            | ApiV1CertificatesArchiveCreateSlaAvailabilityErrorComponent |
            ApiV1CertificatesArchiveCreateSlaTargetErrorComponent |
            ApiV1CertificatesArchiveCreateSloAvailabilityErrorComponent |
            ApiV1CertificatesArchiveCreateSloTargetErrorComponent |
            ApiV1CertificatesArchiveCreateTargetAvailabilityErrorComponent |
            ApiV1CertificatesArchiveCreateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1CertificatesArchiveCreateAnnotationsErrorComponent
        | ApiV1CertificatesArchiveCreateArchivedAtErrorComponent
        | ApiV1CertificatesArchiveCreateArchivedErrorComponent
        | ApiV1CertificatesArchiveCreateArchivedReasonErrorComponent
        | ApiV1CertificatesArchiveCreateCertificateStatusErrorComponent
        | ApiV1CertificatesArchiveCreateCertManagerStatusErrorComponent
        | ApiV1CertificatesArchiveCreateChallengeReasonErrorComponent
        | ApiV1CertificatesArchiveCreateCriticalityErrorComponent
        | ApiV1CertificatesArchiveCreateCurrentChallengeStatusErrorComponent
        | ApiV1CertificatesArchiveCreateCurrentChallengeTypeErrorComponent
        | ApiV1CertificatesArchiveCreateDebugModeErrorComponent
        | ApiV1CertificatesArchiveCreateDisplayNameErrorComponent
        | ApiV1CertificatesArchiveCreateDnsNamesErrorComponent
        | ApiV1CertificatesArchiveCreateFailureReasonErrorComponent
        | ApiV1CertificatesArchiveCreateIpAddressesErrorComponent
        | ApiV1CertificatesArchiveCreateIsReadyErrorComponent
        | ApiV1CertificatesArchiveCreateIssuerGroupErrorComponent
        | ApiV1CertificatesArchiveCreateIssuerKindErrorComponent
        | ApiV1CertificatesArchiveCreateIssuerNameErrorComponent
        | ApiV1CertificatesArchiveCreateK8SClusterErrorComponent
        | ApiV1CertificatesArchiveCreateKindErrorComponent
        | ApiV1CertificatesArchiveCreateLabelsErrorComponent
        | ApiV1CertificatesArchiveCreateLastFailureTimeErrorComponent
        | ApiV1CertificatesArchiveCreateLastSyncedFromClusterErrorComponent
        | ApiV1CertificatesArchiveCreateMetadataErrorComponent
        | ApiV1CertificatesArchiveCreateNameErrorComponent
        | ApiV1CertificatesArchiveCreateNamespaceErrorComponent
        | ApiV1CertificatesArchiveCreateNonFieldErrorsErrorComponent
        | ApiV1CertificatesArchiveCreateNotAfterErrorComponent
        | ApiV1CertificatesArchiveCreateNotBeforeErrorComponent
        | ApiV1CertificatesArchiveCreatePlatformServiceErrorComponent
        | ApiV1CertificatesArchiveCreateProviderErrorComponent
        | ApiV1CertificatesArchiveCreateProviderIdErrorComponent
        | ApiV1CertificatesArchiveCreateProviderReferenceErrorComponent
        | ApiV1CertificatesArchiveCreateReconciliationEnabledErrorComponent
        | ApiV1CertificatesArchiveCreateRenewalTimeErrorComponent
        | ApiV1CertificatesArchiveCreateSecretNameErrorComponent
        | ApiV1CertificatesArchiveCreateSlaAvailabilityErrorComponent
        | ApiV1CertificatesArchiveCreateSlaTargetErrorComponent
        | ApiV1CertificatesArchiveCreateSloAvailabilityErrorComponent
        | ApiV1CertificatesArchiveCreateSloTargetErrorComponent
        | ApiV1CertificatesArchiveCreateTargetAvailabilityErrorComponent
        | ApiV1CertificatesArchiveCreateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_certificates_archive_create_annotations_error_component import (
            ApiV1CertificatesArchiveCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_archived_at_error_component import (
            ApiV1CertificatesArchiveCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_archived_error_component import (
            ApiV1CertificatesArchiveCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_archived_reason_error_component import (
            ApiV1CertificatesArchiveCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_cert_manager_status_error_component import (
            ApiV1CertificatesArchiveCreateCertManagerStatusErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_certificate_status_error_component import (
            ApiV1CertificatesArchiveCreateCertificateStatusErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_challenge_reason_error_component import (
            ApiV1CertificatesArchiveCreateChallengeReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_criticality_error_component import (
            ApiV1CertificatesArchiveCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_current_challenge_status_error_component import (
            ApiV1CertificatesArchiveCreateCurrentChallengeStatusErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_current_challenge_type_error_component import (
            ApiV1CertificatesArchiveCreateCurrentChallengeTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_debug_mode_error_component import (
            ApiV1CertificatesArchiveCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_display_name_error_component import (
            ApiV1CertificatesArchiveCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_dns_names_error_component import (
            ApiV1CertificatesArchiveCreateDnsNamesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_failure_reason_error_component import (
            ApiV1CertificatesArchiveCreateFailureReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_ip_addresses_error_component import (
            ApiV1CertificatesArchiveCreateIpAddressesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_is_ready_error_component import (
            ApiV1CertificatesArchiveCreateIsReadyErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_issuer_group_error_component import (
            ApiV1CertificatesArchiveCreateIssuerGroupErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_issuer_kind_error_component import (
            ApiV1CertificatesArchiveCreateIssuerKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_issuer_name_error_component import (
            ApiV1CertificatesArchiveCreateIssuerNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_k8s_cluster_error_component import (
            ApiV1CertificatesArchiveCreateK8SClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_kind_error_component import (
            ApiV1CertificatesArchiveCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_labels_error_component import (
            ApiV1CertificatesArchiveCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_last_failure_time_error_component import (
            ApiV1CertificatesArchiveCreateLastFailureTimeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_last_synced_from_cluster_error_component import (
            ApiV1CertificatesArchiveCreateLastSyncedFromClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_name_error_component import (
            ApiV1CertificatesArchiveCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_namespace_error_component import (
            ApiV1CertificatesArchiveCreateNamespaceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_non_field_errors_error_component import (
            ApiV1CertificatesArchiveCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_not_after_error_component import (
            ApiV1CertificatesArchiveCreateNotAfterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_not_before_error_component import (
            ApiV1CertificatesArchiveCreateNotBeforeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_platform_service_error_component import (
            ApiV1CertificatesArchiveCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_provider_error_component import (
            ApiV1CertificatesArchiveCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_provider_id_error_component import (
            ApiV1CertificatesArchiveCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_provider_reference_error_component import (
            ApiV1CertificatesArchiveCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_reconciliation_enabled_error_component import (
            ApiV1CertificatesArchiveCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_renewal_time_error_component import (
            ApiV1CertificatesArchiveCreateRenewalTimeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_secret_name_error_component import (
            ApiV1CertificatesArchiveCreateSecretNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_sla_availability_error_component import (
            ApiV1CertificatesArchiveCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_sla_target_error_component import (
            ApiV1CertificatesArchiveCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_slo_availability_error_component import (
            ApiV1CertificatesArchiveCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_slo_target_error_component import (
            ApiV1CertificatesArchiveCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_target_availability_error_component import (
            ApiV1CertificatesArchiveCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_tolerations_error_component import (
            ApiV1CertificatesArchiveCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1CertificatesArchiveCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesArchiveCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesArchiveCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesArchiveCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesArchiveCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesArchiveCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesArchiveCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesArchiveCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesArchiveCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesArchiveCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesArchiveCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesArchiveCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesArchiveCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesArchiveCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesArchiveCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesArchiveCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesArchiveCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesArchiveCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesArchiveCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesArchiveCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesArchiveCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesArchiveCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesArchiveCreateSecretNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesArchiveCreateNamespaceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesArchiveCreateDnsNamesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesArchiveCreateIpAddressesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesArchiveCreateIssuerNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesArchiveCreateIssuerKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesArchiveCreateIssuerGroupErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesArchiveCreateNotBeforeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesArchiveCreateNotAfterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesArchiveCreateRenewalTimeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesArchiveCreateCertificateStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesArchiveCreateIsReadyErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesArchiveCreateCurrentChallengeTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesArchiveCreateCurrentChallengeStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesArchiveCreateChallengeReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesArchiveCreateLastFailureTimeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesArchiveCreateFailureReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesArchiveCreateLastSyncedFromClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesArchiveCreateCertManagerStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesArchiveCreateK8SClusterErrorComponent):
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
        from ..models.api_v1_certificates_archive_create_annotations_error_component import (
            ApiV1CertificatesArchiveCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_archived_at_error_component import (
            ApiV1CertificatesArchiveCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_archived_error_component import (
            ApiV1CertificatesArchiveCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_archived_reason_error_component import (
            ApiV1CertificatesArchiveCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_cert_manager_status_error_component import (
            ApiV1CertificatesArchiveCreateCertManagerStatusErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_certificate_status_error_component import (
            ApiV1CertificatesArchiveCreateCertificateStatusErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_challenge_reason_error_component import (
            ApiV1CertificatesArchiveCreateChallengeReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_criticality_error_component import (
            ApiV1CertificatesArchiveCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_current_challenge_status_error_component import (
            ApiV1CertificatesArchiveCreateCurrentChallengeStatusErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_current_challenge_type_error_component import (
            ApiV1CertificatesArchiveCreateCurrentChallengeTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_debug_mode_error_component import (
            ApiV1CertificatesArchiveCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_display_name_error_component import (
            ApiV1CertificatesArchiveCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_dns_names_error_component import (
            ApiV1CertificatesArchiveCreateDnsNamesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_failure_reason_error_component import (
            ApiV1CertificatesArchiveCreateFailureReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_ip_addresses_error_component import (
            ApiV1CertificatesArchiveCreateIpAddressesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_is_ready_error_component import (
            ApiV1CertificatesArchiveCreateIsReadyErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_issuer_group_error_component import (
            ApiV1CertificatesArchiveCreateIssuerGroupErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_issuer_kind_error_component import (
            ApiV1CertificatesArchiveCreateIssuerKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_issuer_name_error_component import (
            ApiV1CertificatesArchiveCreateIssuerNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_k8s_cluster_error_component import (
            ApiV1CertificatesArchiveCreateK8SClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_kind_error_component import (
            ApiV1CertificatesArchiveCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_labels_error_component import (
            ApiV1CertificatesArchiveCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_last_failure_time_error_component import (
            ApiV1CertificatesArchiveCreateLastFailureTimeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_last_synced_from_cluster_error_component import (
            ApiV1CertificatesArchiveCreateLastSyncedFromClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_metadata_error_component import (
            ApiV1CertificatesArchiveCreateMetadataErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_name_error_component import (
            ApiV1CertificatesArchiveCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_namespace_error_component import (
            ApiV1CertificatesArchiveCreateNamespaceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_non_field_errors_error_component import (
            ApiV1CertificatesArchiveCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_not_after_error_component import (
            ApiV1CertificatesArchiveCreateNotAfterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_not_before_error_component import (
            ApiV1CertificatesArchiveCreateNotBeforeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_platform_service_error_component import (
            ApiV1CertificatesArchiveCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_provider_error_component import (
            ApiV1CertificatesArchiveCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_provider_id_error_component import (
            ApiV1CertificatesArchiveCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_provider_reference_error_component import (
            ApiV1CertificatesArchiveCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_reconciliation_enabled_error_component import (
            ApiV1CertificatesArchiveCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_renewal_time_error_component import (
            ApiV1CertificatesArchiveCreateRenewalTimeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_secret_name_error_component import (
            ApiV1CertificatesArchiveCreateSecretNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_sla_availability_error_component import (
            ApiV1CertificatesArchiveCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_sla_target_error_component import (
            ApiV1CertificatesArchiveCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_slo_availability_error_component import (
            ApiV1CertificatesArchiveCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_slo_target_error_component import (
            ApiV1CertificatesArchiveCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_target_availability_error_component import (
            ApiV1CertificatesArchiveCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_certificates_archive_create_tolerations_error_component import (
            ApiV1CertificatesArchiveCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1CertificatesArchiveCreateAnnotationsErrorComponent
                | ApiV1CertificatesArchiveCreateArchivedAtErrorComponent
                | ApiV1CertificatesArchiveCreateArchivedErrorComponent
                | ApiV1CertificatesArchiveCreateArchivedReasonErrorComponent
                | ApiV1CertificatesArchiveCreateCertificateStatusErrorComponent
                | ApiV1CertificatesArchiveCreateCertManagerStatusErrorComponent
                | ApiV1CertificatesArchiveCreateChallengeReasonErrorComponent
                | ApiV1CertificatesArchiveCreateCriticalityErrorComponent
                | ApiV1CertificatesArchiveCreateCurrentChallengeStatusErrorComponent
                | ApiV1CertificatesArchiveCreateCurrentChallengeTypeErrorComponent
                | ApiV1CertificatesArchiveCreateDebugModeErrorComponent
                | ApiV1CertificatesArchiveCreateDisplayNameErrorComponent
                | ApiV1CertificatesArchiveCreateDnsNamesErrorComponent
                | ApiV1CertificatesArchiveCreateFailureReasonErrorComponent
                | ApiV1CertificatesArchiveCreateIpAddressesErrorComponent
                | ApiV1CertificatesArchiveCreateIsReadyErrorComponent
                | ApiV1CertificatesArchiveCreateIssuerGroupErrorComponent
                | ApiV1CertificatesArchiveCreateIssuerKindErrorComponent
                | ApiV1CertificatesArchiveCreateIssuerNameErrorComponent
                | ApiV1CertificatesArchiveCreateK8SClusterErrorComponent
                | ApiV1CertificatesArchiveCreateKindErrorComponent
                | ApiV1CertificatesArchiveCreateLabelsErrorComponent
                | ApiV1CertificatesArchiveCreateLastFailureTimeErrorComponent
                | ApiV1CertificatesArchiveCreateLastSyncedFromClusterErrorComponent
                | ApiV1CertificatesArchiveCreateMetadataErrorComponent
                | ApiV1CertificatesArchiveCreateNameErrorComponent
                | ApiV1CertificatesArchiveCreateNamespaceErrorComponent
                | ApiV1CertificatesArchiveCreateNonFieldErrorsErrorComponent
                | ApiV1CertificatesArchiveCreateNotAfterErrorComponent
                | ApiV1CertificatesArchiveCreateNotBeforeErrorComponent
                | ApiV1CertificatesArchiveCreatePlatformServiceErrorComponent
                | ApiV1CertificatesArchiveCreateProviderErrorComponent
                | ApiV1CertificatesArchiveCreateProviderIdErrorComponent
                | ApiV1CertificatesArchiveCreateProviderReferenceErrorComponent
                | ApiV1CertificatesArchiveCreateReconciliationEnabledErrorComponent
                | ApiV1CertificatesArchiveCreateRenewalTimeErrorComponent
                | ApiV1CertificatesArchiveCreateSecretNameErrorComponent
                | ApiV1CertificatesArchiveCreateSlaAvailabilityErrorComponent
                | ApiV1CertificatesArchiveCreateSlaTargetErrorComponent
                | ApiV1CertificatesArchiveCreateSloAvailabilityErrorComponent
                | ApiV1CertificatesArchiveCreateSloTargetErrorComponent
                | ApiV1CertificatesArchiveCreateTargetAvailabilityErrorComponent
                | ApiV1CertificatesArchiveCreateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_archive_create_error_type_0 = (
                        ApiV1CertificatesArchiveCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_archive_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_archive_create_error_type_1 = (
                        ApiV1CertificatesArchiveCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_archive_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_archive_create_error_type_2 = (
                        ApiV1CertificatesArchiveCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_archive_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_archive_create_error_type_3 = (
                        ApiV1CertificatesArchiveCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_archive_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_archive_create_error_type_4 = (
                        ApiV1CertificatesArchiveCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_archive_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_archive_create_error_type_5 = (
                        ApiV1CertificatesArchiveCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_archive_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_archive_create_error_type_6 = (
                        ApiV1CertificatesArchiveCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_archive_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_archive_create_error_type_7 = (
                        ApiV1CertificatesArchiveCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_archive_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_archive_create_error_type_8 = (
                        ApiV1CertificatesArchiveCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_archive_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_archive_create_error_type_9 = (
                        ApiV1CertificatesArchiveCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_archive_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_archive_create_error_type_10 = (
                        ApiV1CertificatesArchiveCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_archive_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_archive_create_error_type_11 = (
                        ApiV1CertificatesArchiveCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_archive_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_archive_create_error_type_12 = (
                        ApiV1CertificatesArchiveCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_archive_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_archive_create_error_type_13 = (
                        ApiV1CertificatesArchiveCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_archive_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_archive_create_error_type_14 = (
                        ApiV1CertificatesArchiveCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_archive_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_archive_create_error_type_15 = (
                        ApiV1CertificatesArchiveCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_archive_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_archive_create_error_type_16 = (
                        ApiV1CertificatesArchiveCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_archive_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_archive_create_error_type_17 = (
                        ApiV1CertificatesArchiveCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_archive_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_archive_create_error_type_18 = (
                        ApiV1CertificatesArchiveCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_archive_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_archive_create_error_type_19 = (
                        ApiV1CertificatesArchiveCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_archive_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_archive_create_error_type_20 = (
                        ApiV1CertificatesArchiveCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_archive_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_archive_create_error_type_21 = (
                        ApiV1CertificatesArchiveCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_archive_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_archive_create_error_type_22 = (
                        ApiV1CertificatesArchiveCreateSecretNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_archive_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_archive_create_error_type_23 = (
                        ApiV1CertificatesArchiveCreateNamespaceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_archive_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_archive_create_error_type_24 = (
                        ApiV1CertificatesArchiveCreateDnsNamesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_archive_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_archive_create_error_type_25 = (
                        ApiV1CertificatesArchiveCreateIpAddressesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_archive_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_archive_create_error_type_26 = (
                        ApiV1CertificatesArchiveCreateIssuerNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_archive_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_archive_create_error_type_27 = (
                        ApiV1CertificatesArchiveCreateIssuerKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_archive_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_archive_create_error_type_28 = (
                        ApiV1CertificatesArchiveCreateIssuerGroupErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_archive_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_archive_create_error_type_29 = (
                        ApiV1CertificatesArchiveCreateNotBeforeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_archive_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_archive_create_error_type_30 = (
                        ApiV1CertificatesArchiveCreateNotAfterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_archive_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_archive_create_error_type_31 = (
                        ApiV1CertificatesArchiveCreateRenewalTimeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_archive_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_archive_create_error_type_32 = (
                        ApiV1CertificatesArchiveCreateCertificateStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_archive_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_archive_create_error_type_33 = (
                        ApiV1CertificatesArchiveCreateIsReadyErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_archive_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_archive_create_error_type_34 = (
                        ApiV1CertificatesArchiveCreateCurrentChallengeTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_archive_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_archive_create_error_type_35 = (
                        ApiV1CertificatesArchiveCreateCurrentChallengeStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_archive_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_archive_create_error_type_36 = (
                        ApiV1CertificatesArchiveCreateChallengeReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_archive_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_archive_create_error_type_37 = (
                        ApiV1CertificatesArchiveCreateLastFailureTimeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_archive_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_archive_create_error_type_38 = (
                        ApiV1CertificatesArchiveCreateFailureReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_archive_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_archive_create_error_type_39 = (
                        ApiV1CertificatesArchiveCreateLastSyncedFromClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_archive_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_archive_create_error_type_40 = (
                        ApiV1CertificatesArchiveCreateCertManagerStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_archive_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_archive_create_error_type_41 = (
                        ApiV1CertificatesArchiveCreateK8SClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_archive_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_certificates_archive_create_error_type_42 = (
                    ApiV1CertificatesArchiveCreateMetadataErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_certificates_archive_create_error_type_42

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_certificates_archive_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_certificates_archive_create_validation_error.additional_properties = d
        return api_v1_certificates_archive_create_validation_error

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
