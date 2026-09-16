from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_domains_dnszones_archive_create_annotations_error_component import (
        ApiV1DomainsDnszonesArchiveCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_archive_create_archived_at_error_component import (
        ApiV1DomainsDnszonesArchiveCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_archive_create_archived_by_error_component import (
        ApiV1DomainsDnszonesArchiveCreateArchivedByErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_archive_create_archived_error_component import (
        ApiV1DomainsDnszonesArchiveCreateArchivedErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_archive_create_archived_reason_error_component import (
        ApiV1DomainsDnszonesArchiveCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_archive_create_created_by_component_error_component import (
        ApiV1DomainsDnszonesArchiveCreateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_archive_create_created_by_user_error_component import (
        ApiV1DomainsDnszonesArchiveCreateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_archive_create_credential_id_error_component import (
        ApiV1DomainsDnszonesArchiveCreateCredentialIdErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_archive_create_criticality_error_component import (
        ApiV1DomainsDnszonesArchiveCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_archive_create_debug_mode_error_component import (
        ApiV1DomainsDnszonesArchiveCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_archive_create_default_ttl_error_component import (
        ApiV1DomainsDnszonesArchiveCreateDefaultTtlErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_archive_create_display_name_error_component import (
        ApiV1DomainsDnszonesArchiveCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_archive_create_dnssec_algorithm_error_component import (
        ApiV1DomainsDnszonesArchiveCreateDnssecAlgorithmErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_archive_create_dnssec_cryptokeys_error_component import (
        ApiV1DomainsDnszonesArchiveCreateDnssecCryptokeysErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_archive_create_dnssec_ds_records_error_component import (
        ApiV1DomainsDnszonesArchiveCreateDnssecDsRecordsErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_archive_create_dnssec_enabled_error_component import (
        ApiV1DomainsDnszonesArchiveCreateDnssecEnabledErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_archive_create_dnssec_nsec_3_error_component import (
        ApiV1DomainsDnszonesArchiveCreateDnssecNsec3ErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_archive_create_ds_delegation_synced_error_component import (
        ApiV1DomainsDnszonesArchiveCreateDsDelegationSyncedErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_archive_create_kind_error_component import (
        ApiV1DomainsDnszonesArchiveCreateKindErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_archive_create_labels_error_component import (
        ApiV1DomainsDnszonesArchiveCreateLabelsErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_archive_create_last_reconciliation_duration_seconds_error_component import (
        ApiV1DomainsDnszonesArchiveCreateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_archive_create_managed_by_content_type_error_component import (
        ApiV1DomainsDnszonesArchiveCreateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_archive_create_managed_by_object_id_error_component import (
        ApiV1DomainsDnszonesArchiveCreateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_archive_create_modified_by_user_error_component import (
        ApiV1DomainsDnszonesArchiveCreateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_archive_create_name_error_component import (
        ApiV1DomainsDnszonesArchiveCreateNameErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_archive_create_non_field_errors_error_component import (
        ApiV1DomainsDnszonesArchiveCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_archive_create_ns_delegation_synced_error_component import (
        ApiV1DomainsDnszonesArchiveCreateNsDelegationSyncedErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_archive_create_organization_id_error_component import (
        ApiV1DomainsDnszonesArchiveCreateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_archive_create_platform_dns_record_created_error_component import (
        ApiV1DomainsDnszonesArchiveCreatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_archive_create_platform_service_error_component import (
        ApiV1DomainsDnszonesArchiveCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_archive_create_powerdns_metadata_error_component import (
        ApiV1DomainsDnszonesArchiveCreatePowerdnsMetadataErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_archive_create_primary_zone_error_component import (
        ApiV1DomainsDnszonesArchiveCreatePrimaryZoneErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_archive_create_provider_error_component import (
        ApiV1DomainsDnszonesArchiveCreateProviderErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_archive_create_provider_id_error_component import (
        ApiV1DomainsDnszonesArchiveCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_archive_create_provider_reference_error_component import (
        ApiV1DomainsDnszonesArchiveCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_archive_create_reconciliation_enabled_error_component import (
        ApiV1DomainsDnszonesArchiveCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_archive_create_sla_availability_error_component import (
        ApiV1DomainsDnszonesArchiveCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_archive_create_sla_target_error_component import (
        ApiV1DomainsDnszonesArchiveCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_archive_create_sla_window_days_error_component import (
        ApiV1DomainsDnszonesArchiveCreateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_archive_create_slo_availability_error_component import (
        ApiV1DomainsDnszonesArchiveCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_archive_create_slo_target_error_component import (
        ApiV1DomainsDnszonesArchiveCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_archive_create_slo_window_days_error_component import (
        ApiV1DomainsDnszonesArchiveCreateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_archive_create_sync_from_error_component import (
        ApiV1DomainsDnszonesArchiveCreateSyncFromErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_archive_create_target_availability_error_component import (
        ApiV1DomainsDnszonesArchiveCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_archive_create_tolerations_error_component import (
        ApiV1DomainsDnszonesArchiveCreateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1DomainsDnszonesArchiveCreateValidationError")


@_attrs_define
class ApiV1DomainsDnszonesArchiveCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1DomainsDnszonesArchiveCreateAnnotationsErrorComponent |
            ApiV1DomainsDnszonesArchiveCreateArchivedAtErrorComponent |
            ApiV1DomainsDnszonesArchiveCreateArchivedByErrorComponent |
            ApiV1DomainsDnszonesArchiveCreateArchivedErrorComponent |
            ApiV1DomainsDnszonesArchiveCreateArchivedReasonErrorComponent |
            ApiV1DomainsDnszonesArchiveCreateCreatedByComponentErrorComponent |
            ApiV1DomainsDnszonesArchiveCreateCreatedByUserErrorComponent |
            ApiV1DomainsDnszonesArchiveCreateCredentialIdErrorComponent |
            ApiV1DomainsDnszonesArchiveCreateCriticalityErrorComponent |
            ApiV1DomainsDnszonesArchiveCreateDebugModeErrorComponent |
            ApiV1DomainsDnszonesArchiveCreateDefaultTtlErrorComponent |
            ApiV1DomainsDnszonesArchiveCreateDisplayNameErrorComponent |
            ApiV1DomainsDnszonesArchiveCreateDnssecAlgorithmErrorComponent |
            ApiV1DomainsDnszonesArchiveCreateDnssecCryptokeysErrorComponent |
            ApiV1DomainsDnszonesArchiveCreateDnssecDsRecordsErrorComponent |
            ApiV1DomainsDnszonesArchiveCreateDnssecEnabledErrorComponent |
            ApiV1DomainsDnszonesArchiveCreateDnssecNsec3ErrorComponent |
            ApiV1DomainsDnszonesArchiveCreateDsDelegationSyncedErrorComponent |
            ApiV1DomainsDnszonesArchiveCreateKindErrorComponent | ApiV1DomainsDnszonesArchiveCreateLabelsErrorComponent |
            ApiV1DomainsDnszonesArchiveCreateLastReconciliationDurationSecondsErrorComponent |
            ApiV1DomainsDnszonesArchiveCreateManagedByContentTypeErrorComponent |
            ApiV1DomainsDnszonesArchiveCreateManagedByObjectIdErrorComponent |
            ApiV1DomainsDnszonesArchiveCreateModifiedByUserErrorComponent |
            ApiV1DomainsDnszonesArchiveCreateNameErrorComponent |
            ApiV1DomainsDnszonesArchiveCreateNonFieldErrorsErrorComponent |
            ApiV1DomainsDnszonesArchiveCreateNsDelegationSyncedErrorComponent |
            ApiV1DomainsDnszonesArchiveCreateOrganizationIdErrorComponent |
            ApiV1DomainsDnszonesArchiveCreatePlatformDnsRecordCreatedErrorComponent |
            ApiV1DomainsDnszonesArchiveCreatePlatformServiceErrorComponent |
            ApiV1DomainsDnszonesArchiveCreatePowerdnsMetadataErrorComponent |
            ApiV1DomainsDnszonesArchiveCreatePrimaryZoneErrorComponent |
            ApiV1DomainsDnszonesArchiveCreateProviderErrorComponent |
            ApiV1DomainsDnszonesArchiveCreateProviderIdErrorComponent |
            ApiV1DomainsDnszonesArchiveCreateProviderReferenceErrorComponent |
            ApiV1DomainsDnszonesArchiveCreateReconciliationEnabledErrorComponent |
            ApiV1DomainsDnszonesArchiveCreateSlaAvailabilityErrorComponent |
            ApiV1DomainsDnszonesArchiveCreateSlaTargetErrorComponent |
            ApiV1DomainsDnszonesArchiveCreateSlaWindowDaysErrorComponent |
            ApiV1DomainsDnszonesArchiveCreateSloAvailabilityErrorComponent |
            ApiV1DomainsDnszonesArchiveCreateSloTargetErrorComponent |
            ApiV1DomainsDnszonesArchiveCreateSloWindowDaysErrorComponent |
            ApiV1DomainsDnszonesArchiveCreateSyncFromErrorComponent |
            ApiV1DomainsDnszonesArchiveCreateTargetAvailabilityErrorComponent |
            ApiV1DomainsDnszonesArchiveCreateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1DomainsDnszonesArchiveCreateAnnotationsErrorComponent
        | ApiV1DomainsDnszonesArchiveCreateArchivedAtErrorComponent
        | ApiV1DomainsDnszonesArchiveCreateArchivedByErrorComponent
        | ApiV1DomainsDnszonesArchiveCreateArchivedErrorComponent
        | ApiV1DomainsDnszonesArchiveCreateArchivedReasonErrorComponent
        | ApiV1DomainsDnszonesArchiveCreateCreatedByComponentErrorComponent
        | ApiV1DomainsDnszonesArchiveCreateCreatedByUserErrorComponent
        | ApiV1DomainsDnszonesArchiveCreateCredentialIdErrorComponent
        | ApiV1DomainsDnszonesArchiveCreateCriticalityErrorComponent
        | ApiV1DomainsDnszonesArchiveCreateDebugModeErrorComponent
        | ApiV1DomainsDnszonesArchiveCreateDefaultTtlErrorComponent
        | ApiV1DomainsDnszonesArchiveCreateDisplayNameErrorComponent
        | ApiV1DomainsDnszonesArchiveCreateDnssecAlgorithmErrorComponent
        | ApiV1DomainsDnszonesArchiveCreateDnssecCryptokeysErrorComponent
        | ApiV1DomainsDnszonesArchiveCreateDnssecDsRecordsErrorComponent
        | ApiV1DomainsDnszonesArchiveCreateDnssecEnabledErrorComponent
        | ApiV1DomainsDnszonesArchiveCreateDnssecNsec3ErrorComponent
        | ApiV1DomainsDnszonesArchiveCreateDsDelegationSyncedErrorComponent
        | ApiV1DomainsDnszonesArchiveCreateKindErrorComponent
        | ApiV1DomainsDnszonesArchiveCreateLabelsErrorComponent
        | ApiV1DomainsDnszonesArchiveCreateLastReconciliationDurationSecondsErrorComponent
        | ApiV1DomainsDnszonesArchiveCreateManagedByContentTypeErrorComponent
        | ApiV1DomainsDnszonesArchiveCreateManagedByObjectIdErrorComponent
        | ApiV1DomainsDnszonesArchiveCreateModifiedByUserErrorComponent
        | ApiV1DomainsDnszonesArchiveCreateNameErrorComponent
        | ApiV1DomainsDnszonesArchiveCreateNonFieldErrorsErrorComponent
        | ApiV1DomainsDnszonesArchiveCreateNsDelegationSyncedErrorComponent
        | ApiV1DomainsDnszonesArchiveCreateOrganizationIdErrorComponent
        | ApiV1DomainsDnszonesArchiveCreatePlatformDnsRecordCreatedErrorComponent
        | ApiV1DomainsDnszonesArchiveCreatePlatformServiceErrorComponent
        | ApiV1DomainsDnszonesArchiveCreatePowerdnsMetadataErrorComponent
        | ApiV1DomainsDnszonesArchiveCreatePrimaryZoneErrorComponent
        | ApiV1DomainsDnszonesArchiveCreateProviderErrorComponent
        | ApiV1DomainsDnszonesArchiveCreateProviderIdErrorComponent
        | ApiV1DomainsDnszonesArchiveCreateProviderReferenceErrorComponent
        | ApiV1DomainsDnszonesArchiveCreateReconciliationEnabledErrorComponent
        | ApiV1DomainsDnszonesArchiveCreateSlaAvailabilityErrorComponent
        | ApiV1DomainsDnszonesArchiveCreateSlaTargetErrorComponent
        | ApiV1DomainsDnszonesArchiveCreateSlaWindowDaysErrorComponent
        | ApiV1DomainsDnszonesArchiveCreateSloAvailabilityErrorComponent
        | ApiV1DomainsDnszonesArchiveCreateSloTargetErrorComponent
        | ApiV1DomainsDnszonesArchiveCreateSloWindowDaysErrorComponent
        | ApiV1DomainsDnszonesArchiveCreateSyncFromErrorComponent
        | ApiV1DomainsDnszonesArchiveCreateTargetAvailabilityErrorComponent
        | ApiV1DomainsDnszonesArchiveCreateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_domains_dnszones_archive_create_annotations_error_component import (
            ApiV1DomainsDnszonesArchiveCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_archived_at_error_component import (
            ApiV1DomainsDnszonesArchiveCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_archived_by_error_component import (
            ApiV1DomainsDnszonesArchiveCreateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_archived_error_component import (
            ApiV1DomainsDnszonesArchiveCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_archived_reason_error_component import (
            ApiV1DomainsDnszonesArchiveCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_created_by_component_error_component import (
            ApiV1DomainsDnszonesArchiveCreateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_created_by_user_error_component import (
            ApiV1DomainsDnszonesArchiveCreateCreatedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_credential_id_error_component import (
            ApiV1DomainsDnszonesArchiveCreateCredentialIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_criticality_error_component import (
            ApiV1DomainsDnszonesArchiveCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_debug_mode_error_component import (
            ApiV1DomainsDnszonesArchiveCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_default_ttl_error_component import (
            ApiV1DomainsDnszonesArchiveCreateDefaultTtlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_display_name_error_component import (
            ApiV1DomainsDnszonesArchiveCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_dnssec_algorithm_error_component import (
            ApiV1DomainsDnszonesArchiveCreateDnssecAlgorithmErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_dnssec_cryptokeys_error_component import (
            ApiV1DomainsDnszonesArchiveCreateDnssecCryptokeysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_dnssec_ds_records_error_component import (
            ApiV1DomainsDnszonesArchiveCreateDnssecDsRecordsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_dnssec_enabled_error_component import (
            ApiV1DomainsDnszonesArchiveCreateDnssecEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_dnssec_nsec_3_error_component import (
            ApiV1DomainsDnszonesArchiveCreateDnssecNsec3ErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_ds_delegation_synced_error_component import (
            ApiV1DomainsDnszonesArchiveCreateDsDelegationSyncedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_kind_error_component import (
            ApiV1DomainsDnszonesArchiveCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_labels_error_component import (
            ApiV1DomainsDnszonesArchiveCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1DomainsDnszonesArchiveCreateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_managed_by_content_type_error_component import (
            ApiV1DomainsDnszonesArchiveCreateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_managed_by_object_id_error_component import (
            ApiV1DomainsDnszonesArchiveCreateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_modified_by_user_error_component import (
            ApiV1DomainsDnszonesArchiveCreateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_name_error_component import (
            ApiV1DomainsDnszonesArchiveCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_non_field_errors_error_component import (
            ApiV1DomainsDnszonesArchiveCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_ns_delegation_synced_error_component import (
            ApiV1DomainsDnszonesArchiveCreateNsDelegationSyncedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_organization_id_error_component import (
            ApiV1DomainsDnszonesArchiveCreateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_platform_dns_record_created_error_component import (
            ApiV1DomainsDnszonesArchiveCreatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_platform_service_error_component import (
            ApiV1DomainsDnszonesArchiveCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_powerdns_metadata_error_component import (
            ApiV1DomainsDnszonesArchiveCreatePowerdnsMetadataErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_primary_zone_error_component import (
            ApiV1DomainsDnszonesArchiveCreatePrimaryZoneErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_provider_error_component import (
            ApiV1DomainsDnszonesArchiveCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_provider_id_error_component import (
            ApiV1DomainsDnszonesArchiveCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_provider_reference_error_component import (
            ApiV1DomainsDnszonesArchiveCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_reconciliation_enabled_error_component import (
            ApiV1DomainsDnszonesArchiveCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_sla_availability_error_component import (
            ApiV1DomainsDnszonesArchiveCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_sla_target_error_component import (
            ApiV1DomainsDnszonesArchiveCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_sla_window_days_error_component import (
            ApiV1DomainsDnszonesArchiveCreateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_slo_availability_error_component import (
            ApiV1DomainsDnszonesArchiveCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_slo_target_error_component import (
            ApiV1DomainsDnszonesArchiveCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_slo_window_days_error_component import (
            ApiV1DomainsDnszonesArchiveCreateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_target_availability_error_component import (
            ApiV1DomainsDnszonesArchiveCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_tolerations_error_component import (
            ApiV1DomainsDnszonesArchiveCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1DomainsDnszonesArchiveCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesArchiveCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesArchiveCreateCredentialIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesArchiveCreateOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesArchiveCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesArchiveCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesArchiveCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesArchiveCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesArchiveCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesArchiveCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesArchiveCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1DomainsDnszonesArchiveCreateLastReconciliationDurationSecondsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesArchiveCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesArchiveCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesArchiveCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesArchiveCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesArchiveCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesArchiveCreateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesArchiveCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesArchiveCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesArchiveCreateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesArchiveCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesArchiveCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesArchiveCreateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesArchiveCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesArchiveCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesArchiveCreateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesArchiveCreatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesArchiveCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesArchiveCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesArchiveCreatePrimaryZoneErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesArchiveCreatePowerdnsMetadataErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesArchiveCreateDefaultTtlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesArchiveCreateDnssecEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesArchiveCreateDnssecAlgorithmErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesArchiveCreateDnssecNsec3ErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesArchiveCreateDnssecDsRecordsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesArchiveCreateDnssecCryptokeysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesArchiveCreateNsDelegationSyncedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesArchiveCreateDsDelegationSyncedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesArchiveCreateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesArchiveCreateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesArchiveCreateModifiedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesArchiveCreateCreatedByUserErrorComponent):
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
        from ..models.api_v1_domains_dnszones_archive_create_annotations_error_component import (
            ApiV1DomainsDnszonesArchiveCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_archived_at_error_component import (
            ApiV1DomainsDnszonesArchiveCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_archived_by_error_component import (
            ApiV1DomainsDnszonesArchiveCreateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_archived_error_component import (
            ApiV1DomainsDnszonesArchiveCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_archived_reason_error_component import (
            ApiV1DomainsDnszonesArchiveCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_created_by_component_error_component import (
            ApiV1DomainsDnszonesArchiveCreateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_created_by_user_error_component import (
            ApiV1DomainsDnszonesArchiveCreateCreatedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_credential_id_error_component import (
            ApiV1DomainsDnszonesArchiveCreateCredentialIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_criticality_error_component import (
            ApiV1DomainsDnszonesArchiveCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_debug_mode_error_component import (
            ApiV1DomainsDnszonesArchiveCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_default_ttl_error_component import (
            ApiV1DomainsDnszonesArchiveCreateDefaultTtlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_display_name_error_component import (
            ApiV1DomainsDnszonesArchiveCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_dnssec_algorithm_error_component import (
            ApiV1DomainsDnszonesArchiveCreateDnssecAlgorithmErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_dnssec_cryptokeys_error_component import (
            ApiV1DomainsDnszonesArchiveCreateDnssecCryptokeysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_dnssec_ds_records_error_component import (
            ApiV1DomainsDnszonesArchiveCreateDnssecDsRecordsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_dnssec_enabled_error_component import (
            ApiV1DomainsDnszonesArchiveCreateDnssecEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_dnssec_nsec_3_error_component import (
            ApiV1DomainsDnszonesArchiveCreateDnssecNsec3ErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_ds_delegation_synced_error_component import (
            ApiV1DomainsDnszonesArchiveCreateDsDelegationSyncedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_kind_error_component import (
            ApiV1DomainsDnszonesArchiveCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_labels_error_component import (
            ApiV1DomainsDnszonesArchiveCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1DomainsDnszonesArchiveCreateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_managed_by_content_type_error_component import (
            ApiV1DomainsDnszonesArchiveCreateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_managed_by_object_id_error_component import (
            ApiV1DomainsDnszonesArchiveCreateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_modified_by_user_error_component import (
            ApiV1DomainsDnszonesArchiveCreateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_name_error_component import (
            ApiV1DomainsDnszonesArchiveCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_non_field_errors_error_component import (
            ApiV1DomainsDnszonesArchiveCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_ns_delegation_synced_error_component import (
            ApiV1DomainsDnszonesArchiveCreateNsDelegationSyncedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_organization_id_error_component import (
            ApiV1DomainsDnszonesArchiveCreateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_platform_dns_record_created_error_component import (
            ApiV1DomainsDnszonesArchiveCreatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_platform_service_error_component import (
            ApiV1DomainsDnszonesArchiveCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_powerdns_metadata_error_component import (
            ApiV1DomainsDnszonesArchiveCreatePowerdnsMetadataErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_primary_zone_error_component import (
            ApiV1DomainsDnszonesArchiveCreatePrimaryZoneErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_provider_error_component import (
            ApiV1DomainsDnszonesArchiveCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_provider_id_error_component import (
            ApiV1DomainsDnszonesArchiveCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_provider_reference_error_component import (
            ApiV1DomainsDnszonesArchiveCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_reconciliation_enabled_error_component import (
            ApiV1DomainsDnszonesArchiveCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_sla_availability_error_component import (
            ApiV1DomainsDnszonesArchiveCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_sla_target_error_component import (
            ApiV1DomainsDnszonesArchiveCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_sla_window_days_error_component import (
            ApiV1DomainsDnszonesArchiveCreateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_slo_availability_error_component import (
            ApiV1DomainsDnszonesArchiveCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_slo_target_error_component import (
            ApiV1DomainsDnszonesArchiveCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_slo_window_days_error_component import (
            ApiV1DomainsDnszonesArchiveCreateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_sync_from_error_component import (
            ApiV1DomainsDnszonesArchiveCreateSyncFromErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_target_availability_error_component import (
            ApiV1DomainsDnszonesArchiveCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_archive_create_tolerations_error_component import (
            ApiV1DomainsDnszonesArchiveCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1DomainsDnszonesArchiveCreateAnnotationsErrorComponent
                | ApiV1DomainsDnszonesArchiveCreateArchivedAtErrorComponent
                | ApiV1DomainsDnszonesArchiveCreateArchivedByErrorComponent
                | ApiV1DomainsDnszonesArchiveCreateArchivedErrorComponent
                | ApiV1DomainsDnszonesArchiveCreateArchivedReasonErrorComponent
                | ApiV1DomainsDnszonesArchiveCreateCreatedByComponentErrorComponent
                | ApiV1DomainsDnszonesArchiveCreateCreatedByUserErrorComponent
                | ApiV1DomainsDnszonesArchiveCreateCredentialIdErrorComponent
                | ApiV1DomainsDnszonesArchiveCreateCriticalityErrorComponent
                | ApiV1DomainsDnszonesArchiveCreateDebugModeErrorComponent
                | ApiV1DomainsDnszonesArchiveCreateDefaultTtlErrorComponent
                | ApiV1DomainsDnszonesArchiveCreateDisplayNameErrorComponent
                | ApiV1DomainsDnszonesArchiveCreateDnssecAlgorithmErrorComponent
                | ApiV1DomainsDnszonesArchiveCreateDnssecCryptokeysErrorComponent
                | ApiV1DomainsDnszonesArchiveCreateDnssecDsRecordsErrorComponent
                | ApiV1DomainsDnszonesArchiveCreateDnssecEnabledErrorComponent
                | ApiV1DomainsDnszonesArchiveCreateDnssecNsec3ErrorComponent
                | ApiV1DomainsDnszonesArchiveCreateDsDelegationSyncedErrorComponent
                | ApiV1DomainsDnszonesArchiveCreateKindErrorComponent
                | ApiV1DomainsDnszonesArchiveCreateLabelsErrorComponent
                | ApiV1DomainsDnszonesArchiveCreateLastReconciliationDurationSecondsErrorComponent
                | ApiV1DomainsDnszonesArchiveCreateManagedByContentTypeErrorComponent
                | ApiV1DomainsDnszonesArchiveCreateManagedByObjectIdErrorComponent
                | ApiV1DomainsDnszonesArchiveCreateModifiedByUserErrorComponent
                | ApiV1DomainsDnszonesArchiveCreateNameErrorComponent
                | ApiV1DomainsDnszonesArchiveCreateNonFieldErrorsErrorComponent
                | ApiV1DomainsDnszonesArchiveCreateNsDelegationSyncedErrorComponent
                | ApiV1DomainsDnszonesArchiveCreateOrganizationIdErrorComponent
                | ApiV1DomainsDnszonesArchiveCreatePlatformDnsRecordCreatedErrorComponent
                | ApiV1DomainsDnszonesArchiveCreatePlatformServiceErrorComponent
                | ApiV1DomainsDnszonesArchiveCreatePowerdnsMetadataErrorComponent
                | ApiV1DomainsDnszonesArchiveCreatePrimaryZoneErrorComponent
                | ApiV1DomainsDnszonesArchiveCreateProviderErrorComponent
                | ApiV1DomainsDnszonesArchiveCreateProviderIdErrorComponent
                | ApiV1DomainsDnszonesArchiveCreateProviderReferenceErrorComponent
                | ApiV1DomainsDnszonesArchiveCreateReconciliationEnabledErrorComponent
                | ApiV1DomainsDnszonesArchiveCreateSlaAvailabilityErrorComponent
                | ApiV1DomainsDnszonesArchiveCreateSlaTargetErrorComponent
                | ApiV1DomainsDnszonesArchiveCreateSlaWindowDaysErrorComponent
                | ApiV1DomainsDnszonesArchiveCreateSloAvailabilityErrorComponent
                | ApiV1DomainsDnszonesArchiveCreateSloTargetErrorComponent
                | ApiV1DomainsDnszonesArchiveCreateSloWindowDaysErrorComponent
                | ApiV1DomainsDnszonesArchiveCreateSyncFromErrorComponent
                | ApiV1DomainsDnszonesArchiveCreateTargetAvailabilityErrorComponent
                | ApiV1DomainsDnszonesArchiveCreateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_archive_create_error_type_0 = (
                        ApiV1DomainsDnszonesArchiveCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_archive_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_archive_create_error_type_1 = (
                        ApiV1DomainsDnszonesArchiveCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_archive_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_archive_create_error_type_2 = (
                        ApiV1DomainsDnszonesArchiveCreateCredentialIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_archive_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_archive_create_error_type_3 = (
                        ApiV1DomainsDnszonesArchiveCreateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_archive_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_archive_create_error_type_4 = (
                        ApiV1DomainsDnszonesArchiveCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_archive_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_archive_create_error_type_5 = (
                        ApiV1DomainsDnszonesArchiveCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_archive_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_archive_create_error_type_6 = (
                        ApiV1DomainsDnszonesArchiveCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_archive_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_archive_create_error_type_7 = (
                        ApiV1DomainsDnszonesArchiveCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_archive_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_archive_create_error_type_8 = (
                        ApiV1DomainsDnszonesArchiveCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_archive_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_archive_create_error_type_9 = (
                        ApiV1DomainsDnszonesArchiveCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_archive_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_archive_create_error_type_10 = (
                        ApiV1DomainsDnszonesArchiveCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_archive_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_archive_create_error_type_11 = (
                        ApiV1DomainsDnszonesArchiveCreateLastReconciliationDurationSecondsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_archive_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_archive_create_error_type_12 = (
                        ApiV1DomainsDnszonesArchiveCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_archive_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_archive_create_error_type_13 = (
                        ApiV1DomainsDnszonesArchiveCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_archive_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_archive_create_error_type_14 = (
                        ApiV1DomainsDnszonesArchiveCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_archive_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_archive_create_error_type_15 = (
                        ApiV1DomainsDnszonesArchiveCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_archive_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_archive_create_error_type_16 = (
                        ApiV1DomainsDnszonesArchiveCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_archive_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_archive_create_error_type_17 = (
                        ApiV1DomainsDnszonesArchiveCreateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_archive_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_archive_create_error_type_18 = (
                        ApiV1DomainsDnszonesArchiveCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_archive_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_archive_create_error_type_19 = (
                        ApiV1DomainsDnszonesArchiveCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_archive_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_archive_create_error_type_20 = (
                        ApiV1DomainsDnszonesArchiveCreateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_archive_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_archive_create_error_type_21 = (
                        ApiV1DomainsDnszonesArchiveCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_archive_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_archive_create_error_type_22 = (
                        ApiV1DomainsDnszonesArchiveCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_archive_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_archive_create_error_type_23 = (
                        ApiV1DomainsDnszonesArchiveCreateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_archive_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_archive_create_error_type_24 = (
                        ApiV1DomainsDnszonesArchiveCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_archive_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_archive_create_error_type_25 = (
                        ApiV1DomainsDnszonesArchiveCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_archive_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_archive_create_error_type_26 = (
                        ApiV1DomainsDnszonesArchiveCreateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_archive_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_archive_create_error_type_27 = (
                        ApiV1DomainsDnszonesArchiveCreatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_archive_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_archive_create_error_type_28 = (
                        ApiV1DomainsDnszonesArchiveCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_archive_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_archive_create_error_type_29 = (
                        ApiV1DomainsDnszonesArchiveCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_archive_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_archive_create_error_type_30 = (
                        ApiV1DomainsDnszonesArchiveCreatePrimaryZoneErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_archive_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_archive_create_error_type_31 = (
                        ApiV1DomainsDnszonesArchiveCreatePowerdnsMetadataErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_archive_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_archive_create_error_type_32 = (
                        ApiV1DomainsDnszonesArchiveCreateDefaultTtlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_archive_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_archive_create_error_type_33 = (
                        ApiV1DomainsDnszonesArchiveCreateDnssecEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_archive_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_archive_create_error_type_34 = (
                        ApiV1DomainsDnszonesArchiveCreateDnssecAlgorithmErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_archive_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_archive_create_error_type_35 = (
                        ApiV1DomainsDnszonesArchiveCreateDnssecNsec3ErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_archive_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_archive_create_error_type_36 = (
                        ApiV1DomainsDnszonesArchiveCreateDnssecDsRecordsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_archive_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_archive_create_error_type_37 = (
                        ApiV1DomainsDnszonesArchiveCreateDnssecCryptokeysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_archive_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_archive_create_error_type_38 = (
                        ApiV1DomainsDnszonesArchiveCreateNsDelegationSyncedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_archive_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_archive_create_error_type_39 = (
                        ApiV1DomainsDnszonesArchiveCreateDsDelegationSyncedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_archive_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_archive_create_error_type_40 = (
                        ApiV1DomainsDnszonesArchiveCreateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_archive_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_archive_create_error_type_41 = (
                        ApiV1DomainsDnszonesArchiveCreateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_archive_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_archive_create_error_type_42 = (
                        ApiV1DomainsDnszonesArchiveCreateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_archive_create_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_archive_create_error_type_43 = (
                        ApiV1DomainsDnszonesArchiveCreateCreatedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_archive_create_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_domains_dnszones_archive_create_error_type_44 = (
                    ApiV1DomainsDnszonesArchiveCreateSyncFromErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_domains_dnszones_archive_create_error_type_44

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_domains_dnszones_archive_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_domains_dnszones_archive_create_validation_error.additional_properties = d
        return api_v1_domains_dnszones_archive_create_validation_error

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
