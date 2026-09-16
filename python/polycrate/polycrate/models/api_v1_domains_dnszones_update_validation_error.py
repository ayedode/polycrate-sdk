from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_domains_dnszones_update_annotations_error_component import (
        ApiV1DomainsDnszonesUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_update_archived_at_error_component import (
        ApiV1DomainsDnszonesUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_update_archived_by_error_component import (
        ApiV1DomainsDnszonesUpdateArchivedByErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_update_archived_error_component import (
        ApiV1DomainsDnszonesUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_update_archived_reason_error_component import (
        ApiV1DomainsDnszonesUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_update_created_by_component_error_component import (
        ApiV1DomainsDnszonesUpdateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_update_created_by_user_error_component import (
        ApiV1DomainsDnszonesUpdateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_update_credential_id_error_component import (
        ApiV1DomainsDnszonesUpdateCredentialIdErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_update_criticality_error_component import (
        ApiV1DomainsDnszonesUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_update_debug_mode_error_component import (
        ApiV1DomainsDnszonesUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_update_default_ttl_error_component import (
        ApiV1DomainsDnszonesUpdateDefaultTtlErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_update_display_name_error_component import (
        ApiV1DomainsDnszonesUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_update_dnssec_algorithm_error_component import (
        ApiV1DomainsDnszonesUpdateDnssecAlgorithmErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_update_dnssec_cryptokeys_error_component import (
        ApiV1DomainsDnszonesUpdateDnssecCryptokeysErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_update_dnssec_ds_records_error_component import (
        ApiV1DomainsDnszonesUpdateDnssecDsRecordsErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_update_dnssec_enabled_error_component import (
        ApiV1DomainsDnszonesUpdateDnssecEnabledErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_update_dnssec_nsec_3_error_component import (
        ApiV1DomainsDnszonesUpdateDnssecNsec3ErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_update_ds_delegation_synced_error_component import (
        ApiV1DomainsDnszonesUpdateDsDelegationSyncedErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_update_kind_error_component import (
        ApiV1DomainsDnszonesUpdateKindErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_update_labels_error_component import (
        ApiV1DomainsDnszonesUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_update_last_reconciliation_duration_seconds_error_component import (
        ApiV1DomainsDnszonesUpdateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_update_managed_by_content_type_error_component import (
        ApiV1DomainsDnszonesUpdateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_update_managed_by_object_id_error_component import (
        ApiV1DomainsDnszonesUpdateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_update_modified_by_user_error_component import (
        ApiV1DomainsDnszonesUpdateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_update_name_error_component import (
        ApiV1DomainsDnszonesUpdateNameErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_update_non_field_errors_error_component import (
        ApiV1DomainsDnszonesUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_update_ns_delegation_synced_error_component import (
        ApiV1DomainsDnszonesUpdateNsDelegationSyncedErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_update_organization_id_error_component import (
        ApiV1DomainsDnszonesUpdateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_update_platform_dns_record_created_error_component import (
        ApiV1DomainsDnszonesUpdatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_update_platform_service_error_component import (
        ApiV1DomainsDnszonesUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_update_powerdns_metadata_error_component import (
        ApiV1DomainsDnszonesUpdatePowerdnsMetadataErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_update_primary_zone_error_component import (
        ApiV1DomainsDnszonesUpdatePrimaryZoneErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_update_provider_error_component import (
        ApiV1DomainsDnszonesUpdateProviderErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_update_provider_id_error_component import (
        ApiV1DomainsDnszonesUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_update_provider_reference_error_component import (
        ApiV1DomainsDnszonesUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_update_reconciliation_enabled_error_component import (
        ApiV1DomainsDnszonesUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_update_sla_availability_error_component import (
        ApiV1DomainsDnszonesUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_update_sla_target_error_component import (
        ApiV1DomainsDnszonesUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_update_sla_window_days_error_component import (
        ApiV1DomainsDnszonesUpdateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_update_slo_availability_error_component import (
        ApiV1DomainsDnszonesUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_update_slo_target_error_component import (
        ApiV1DomainsDnszonesUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_update_slo_window_days_error_component import (
        ApiV1DomainsDnszonesUpdateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_update_sync_from_error_component import (
        ApiV1DomainsDnszonesUpdateSyncFromErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_update_target_availability_error_component import (
        ApiV1DomainsDnszonesUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_update_tolerations_error_component import (
        ApiV1DomainsDnszonesUpdateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1DomainsDnszonesUpdateValidationError")


@_attrs_define
class ApiV1DomainsDnszonesUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1DomainsDnszonesUpdateAnnotationsErrorComponent |
            ApiV1DomainsDnszonesUpdateArchivedAtErrorComponent | ApiV1DomainsDnszonesUpdateArchivedByErrorComponent |
            ApiV1DomainsDnszonesUpdateArchivedErrorComponent | ApiV1DomainsDnszonesUpdateArchivedReasonErrorComponent |
            ApiV1DomainsDnszonesUpdateCreatedByComponentErrorComponent |
            ApiV1DomainsDnszonesUpdateCreatedByUserErrorComponent | ApiV1DomainsDnszonesUpdateCredentialIdErrorComponent |
            ApiV1DomainsDnszonesUpdateCriticalityErrorComponent | ApiV1DomainsDnszonesUpdateDebugModeErrorComponent |
            ApiV1DomainsDnszonesUpdateDefaultTtlErrorComponent | ApiV1DomainsDnszonesUpdateDisplayNameErrorComponent |
            ApiV1DomainsDnszonesUpdateDnssecAlgorithmErrorComponent |
            ApiV1DomainsDnszonesUpdateDnssecCryptokeysErrorComponent |
            ApiV1DomainsDnszonesUpdateDnssecDsRecordsErrorComponent | ApiV1DomainsDnszonesUpdateDnssecEnabledErrorComponent
            | ApiV1DomainsDnszonesUpdateDnssecNsec3ErrorComponent |
            ApiV1DomainsDnszonesUpdateDsDelegationSyncedErrorComponent | ApiV1DomainsDnszonesUpdateKindErrorComponent |
            ApiV1DomainsDnszonesUpdateLabelsErrorComponent |
            ApiV1DomainsDnszonesUpdateLastReconciliationDurationSecondsErrorComponent |
            ApiV1DomainsDnszonesUpdateManagedByContentTypeErrorComponent |
            ApiV1DomainsDnszonesUpdateManagedByObjectIdErrorComponent |
            ApiV1DomainsDnszonesUpdateModifiedByUserErrorComponent | ApiV1DomainsDnszonesUpdateNameErrorComponent |
            ApiV1DomainsDnszonesUpdateNonFieldErrorsErrorComponent |
            ApiV1DomainsDnszonesUpdateNsDelegationSyncedErrorComponent |
            ApiV1DomainsDnszonesUpdateOrganizationIdErrorComponent |
            ApiV1DomainsDnszonesUpdatePlatformDnsRecordCreatedErrorComponent |
            ApiV1DomainsDnszonesUpdatePlatformServiceErrorComponent |
            ApiV1DomainsDnszonesUpdatePowerdnsMetadataErrorComponent | ApiV1DomainsDnszonesUpdatePrimaryZoneErrorComponent |
            ApiV1DomainsDnszonesUpdateProviderErrorComponent | ApiV1DomainsDnszonesUpdateProviderIdErrorComponent |
            ApiV1DomainsDnszonesUpdateProviderReferenceErrorComponent |
            ApiV1DomainsDnszonesUpdateReconciliationEnabledErrorComponent |
            ApiV1DomainsDnszonesUpdateSlaAvailabilityErrorComponent | ApiV1DomainsDnszonesUpdateSlaTargetErrorComponent |
            ApiV1DomainsDnszonesUpdateSlaWindowDaysErrorComponent | ApiV1DomainsDnszonesUpdateSloAvailabilityErrorComponent
            | ApiV1DomainsDnszonesUpdateSloTargetErrorComponent | ApiV1DomainsDnszonesUpdateSloWindowDaysErrorComponent |
            ApiV1DomainsDnszonesUpdateSyncFromErrorComponent | ApiV1DomainsDnszonesUpdateTargetAvailabilityErrorComponent |
            ApiV1DomainsDnszonesUpdateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1DomainsDnszonesUpdateAnnotationsErrorComponent
        | ApiV1DomainsDnszonesUpdateArchivedAtErrorComponent
        | ApiV1DomainsDnszonesUpdateArchivedByErrorComponent
        | ApiV1DomainsDnszonesUpdateArchivedErrorComponent
        | ApiV1DomainsDnszonesUpdateArchivedReasonErrorComponent
        | ApiV1DomainsDnszonesUpdateCreatedByComponentErrorComponent
        | ApiV1DomainsDnszonesUpdateCreatedByUserErrorComponent
        | ApiV1DomainsDnszonesUpdateCredentialIdErrorComponent
        | ApiV1DomainsDnszonesUpdateCriticalityErrorComponent
        | ApiV1DomainsDnszonesUpdateDebugModeErrorComponent
        | ApiV1DomainsDnszonesUpdateDefaultTtlErrorComponent
        | ApiV1DomainsDnszonesUpdateDisplayNameErrorComponent
        | ApiV1DomainsDnszonesUpdateDnssecAlgorithmErrorComponent
        | ApiV1DomainsDnszonesUpdateDnssecCryptokeysErrorComponent
        | ApiV1DomainsDnszonesUpdateDnssecDsRecordsErrorComponent
        | ApiV1DomainsDnszonesUpdateDnssecEnabledErrorComponent
        | ApiV1DomainsDnszonesUpdateDnssecNsec3ErrorComponent
        | ApiV1DomainsDnszonesUpdateDsDelegationSyncedErrorComponent
        | ApiV1DomainsDnszonesUpdateKindErrorComponent
        | ApiV1DomainsDnszonesUpdateLabelsErrorComponent
        | ApiV1DomainsDnszonesUpdateLastReconciliationDurationSecondsErrorComponent
        | ApiV1DomainsDnszonesUpdateManagedByContentTypeErrorComponent
        | ApiV1DomainsDnszonesUpdateManagedByObjectIdErrorComponent
        | ApiV1DomainsDnszonesUpdateModifiedByUserErrorComponent
        | ApiV1DomainsDnszonesUpdateNameErrorComponent
        | ApiV1DomainsDnszonesUpdateNonFieldErrorsErrorComponent
        | ApiV1DomainsDnszonesUpdateNsDelegationSyncedErrorComponent
        | ApiV1DomainsDnszonesUpdateOrganizationIdErrorComponent
        | ApiV1DomainsDnszonesUpdatePlatformDnsRecordCreatedErrorComponent
        | ApiV1DomainsDnszonesUpdatePlatformServiceErrorComponent
        | ApiV1DomainsDnszonesUpdatePowerdnsMetadataErrorComponent
        | ApiV1DomainsDnszonesUpdatePrimaryZoneErrorComponent
        | ApiV1DomainsDnszonesUpdateProviderErrorComponent
        | ApiV1DomainsDnszonesUpdateProviderIdErrorComponent
        | ApiV1DomainsDnszonesUpdateProviderReferenceErrorComponent
        | ApiV1DomainsDnszonesUpdateReconciliationEnabledErrorComponent
        | ApiV1DomainsDnszonesUpdateSlaAvailabilityErrorComponent
        | ApiV1DomainsDnszonesUpdateSlaTargetErrorComponent
        | ApiV1DomainsDnszonesUpdateSlaWindowDaysErrorComponent
        | ApiV1DomainsDnszonesUpdateSloAvailabilityErrorComponent
        | ApiV1DomainsDnszonesUpdateSloTargetErrorComponent
        | ApiV1DomainsDnszonesUpdateSloWindowDaysErrorComponent
        | ApiV1DomainsDnszonesUpdateSyncFromErrorComponent
        | ApiV1DomainsDnszonesUpdateTargetAvailabilityErrorComponent
        | ApiV1DomainsDnszonesUpdateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_domains_dnszones_update_annotations_error_component import (
            ApiV1DomainsDnszonesUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_archived_at_error_component import (
            ApiV1DomainsDnszonesUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_archived_by_error_component import (
            ApiV1DomainsDnszonesUpdateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_archived_error_component import (
            ApiV1DomainsDnszonesUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_archived_reason_error_component import (
            ApiV1DomainsDnszonesUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_created_by_component_error_component import (
            ApiV1DomainsDnszonesUpdateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_created_by_user_error_component import (
            ApiV1DomainsDnszonesUpdateCreatedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_credential_id_error_component import (
            ApiV1DomainsDnszonesUpdateCredentialIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_criticality_error_component import (
            ApiV1DomainsDnszonesUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_debug_mode_error_component import (
            ApiV1DomainsDnszonesUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_default_ttl_error_component import (
            ApiV1DomainsDnszonesUpdateDefaultTtlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_display_name_error_component import (
            ApiV1DomainsDnszonesUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_dnssec_algorithm_error_component import (
            ApiV1DomainsDnszonesUpdateDnssecAlgorithmErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_dnssec_cryptokeys_error_component import (
            ApiV1DomainsDnszonesUpdateDnssecCryptokeysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_dnssec_ds_records_error_component import (
            ApiV1DomainsDnszonesUpdateDnssecDsRecordsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_dnssec_enabled_error_component import (
            ApiV1DomainsDnszonesUpdateDnssecEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_dnssec_nsec_3_error_component import (
            ApiV1DomainsDnszonesUpdateDnssecNsec3ErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_ds_delegation_synced_error_component import (
            ApiV1DomainsDnszonesUpdateDsDelegationSyncedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_kind_error_component import (
            ApiV1DomainsDnszonesUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_labels_error_component import (
            ApiV1DomainsDnszonesUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_last_reconciliation_duration_seconds_error_component import (
            ApiV1DomainsDnszonesUpdateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_managed_by_content_type_error_component import (
            ApiV1DomainsDnszonesUpdateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_managed_by_object_id_error_component import (
            ApiV1DomainsDnszonesUpdateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_modified_by_user_error_component import (
            ApiV1DomainsDnszonesUpdateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_name_error_component import (
            ApiV1DomainsDnszonesUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_non_field_errors_error_component import (
            ApiV1DomainsDnszonesUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_ns_delegation_synced_error_component import (
            ApiV1DomainsDnszonesUpdateNsDelegationSyncedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_organization_id_error_component import (
            ApiV1DomainsDnszonesUpdateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_platform_dns_record_created_error_component import (
            ApiV1DomainsDnszonesUpdatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_platform_service_error_component import (
            ApiV1DomainsDnszonesUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_powerdns_metadata_error_component import (
            ApiV1DomainsDnszonesUpdatePowerdnsMetadataErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_primary_zone_error_component import (
            ApiV1DomainsDnszonesUpdatePrimaryZoneErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_provider_error_component import (
            ApiV1DomainsDnszonesUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_provider_id_error_component import (
            ApiV1DomainsDnszonesUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_provider_reference_error_component import (
            ApiV1DomainsDnszonesUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_reconciliation_enabled_error_component import (
            ApiV1DomainsDnszonesUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_sla_availability_error_component import (
            ApiV1DomainsDnszonesUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_sla_target_error_component import (
            ApiV1DomainsDnszonesUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_sla_window_days_error_component import (
            ApiV1DomainsDnszonesUpdateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_slo_availability_error_component import (
            ApiV1DomainsDnszonesUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_slo_target_error_component import (
            ApiV1DomainsDnszonesUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_slo_window_days_error_component import (
            ApiV1DomainsDnszonesUpdateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_target_availability_error_component import (
            ApiV1DomainsDnszonesUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_tolerations_error_component import (
            ApiV1DomainsDnszonesUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1DomainsDnszonesUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesUpdateCredentialIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesUpdateOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1DomainsDnszonesUpdateLastReconciliationDurationSecondsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesUpdateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesUpdateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesUpdateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesUpdateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesUpdatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesUpdatePrimaryZoneErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesUpdatePowerdnsMetadataErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesUpdateDefaultTtlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesUpdateDnssecEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesUpdateDnssecAlgorithmErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesUpdateDnssecNsec3ErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesUpdateDnssecDsRecordsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesUpdateDnssecCryptokeysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesUpdateNsDelegationSyncedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesUpdateDsDelegationSyncedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesUpdateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesUpdateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesUpdateModifiedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesUpdateCreatedByUserErrorComponent):
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
        from ..models.api_v1_domains_dnszones_update_annotations_error_component import (
            ApiV1DomainsDnszonesUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_archived_at_error_component import (
            ApiV1DomainsDnszonesUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_archived_by_error_component import (
            ApiV1DomainsDnszonesUpdateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_archived_error_component import (
            ApiV1DomainsDnszonesUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_archived_reason_error_component import (
            ApiV1DomainsDnszonesUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_created_by_component_error_component import (
            ApiV1DomainsDnszonesUpdateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_created_by_user_error_component import (
            ApiV1DomainsDnszonesUpdateCreatedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_credential_id_error_component import (
            ApiV1DomainsDnszonesUpdateCredentialIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_criticality_error_component import (
            ApiV1DomainsDnszonesUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_debug_mode_error_component import (
            ApiV1DomainsDnszonesUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_default_ttl_error_component import (
            ApiV1DomainsDnszonesUpdateDefaultTtlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_display_name_error_component import (
            ApiV1DomainsDnszonesUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_dnssec_algorithm_error_component import (
            ApiV1DomainsDnszonesUpdateDnssecAlgorithmErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_dnssec_cryptokeys_error_component import (
            ApiV1DomainsDnszonesUpdateDnssecCryptokeysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_dnssec_ds_records_error_component import (
            ApiV1DomainsDnszonesUpdateDnssecDsRecordsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_dnssec_enabled_error_component import (
            ApiV1DomainsDnszonesUpdateDnssecEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_dnssec_nsec_3_error_component import (
            ApiV1DomainsDnszonesUpdateDnssecNsec3ErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_ds_delegation_synced_error_component import (
            ApiV1DomainsDnszonesUpdateDsDelegationSyncedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_kind_error_component import (
            ApiV1DomainsDnszonesUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_labels_error_component import (
            ApiV1DomainsDnszonesUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_last_reconciliation_duration_seconds_error_component import (
            ApiV1DomainsDnszonesUpdateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_managed_by_content_type_error_component import (
            ApiV1DomainsDnszonesUpdateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_managed_by_object_id_error_component import (
            ApiV1DomainsDnszonesUpdateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_modified_by_user_error_component import (
            ApiV1DomainsDnszonesUpdateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_name_error_component import (
            ApiV1DomainsDnszonesUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_non_field_errors_error_component import (
            ApiV1DomainsDnszonesUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_ns_delegation_synced_error_component import (
            ApiV1DomainsDnszonesUpdateNsDelegationSyncedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_organization_id_error_component import (
            ApiV1DomainsDnszonesUpdateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_platform_dns_record_created_error_component import (
            ApiV1DomainsDnszonesUpdatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_platform_service_error_component import (
            ApiV1DomainsDnszonesUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_powerdns_metadata_error_component import (
            ApiV1DomainsDnszonesUpdatePowerdnsMetadataErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_primary_zone_error_component import (
            ApiV1DomainsDnszonesUpdatePrimaryZoneErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_provider_error_component import (
            ApiV1DomainsDnszonesUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_provider_id_error_component import (
            ApiV1DomainsDnszonesUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_provider_reference_error_component import (
            ApiV1DomainsDnszonesUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_reconciliation_enabled_error_component import (
            ApiV1DomainsDnszonesUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_sla_availability_error_component import (
            ApiV1DomainsDnszonesUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_sla_target_error_component import (
            ApiV1DomainsDnszonesUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_sla_window_days_error_component import (
            ApiV1DomainsDnszonesUpdateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_slo_availability_error_component import (
            ApiV1DomainsDnszonesUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_slo_target_error_component import (
            ApiV1DomainsDnszonesUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_slo_window_days_error_component import (
            ApiV1DomainsDnszonesUpdateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_sync_from_error_component import (
            ApiV1DomainsDnszonesUpdateSyncFromErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_target_availability_error_component import (
            ApiV1DomainsDnszonesUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_update_tolerations_error_component import (
            ApiV1DomainsDnszonesUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1DomainsDnszonesUpdateAnnotationsErrorComponent
                | ApiV1DomainsDnszonesUpdateArchivedAtErrorComponent
                | ApiV1DomainsDnszonesUpdateArchivedByErrorComponent
                | ApiV1DomainsDnszonesUpdateArchivedErrorComponent
                | ApiV1DomainsDnszonesUpdateArchivedReasonErrorComponent
                | ApiV1DomainsDnszonesUpdateCreatedByComponentErrorComponent
                | ApiV1DomainsDnszonesUpdateCreatedByUserErrorComponent
                | ApiV1DomainsDnszonesUpdateCredentialIdErrorComponent
                | ApiV1DomainsDnszonesUpdateCriticalityErrorComponent
                | ApiV1DomainsDnszonesUpdateDebugModeErrorComponent
                | ApiV1DomainsDnszonesUpdateDefaultTtlErrorComponent
                | ApiV1DomainsDnszonesUpdateDisplayNameErrorComponent
                | ApiV1DomainsDnszonesUpdateDnssecAlgorithmErrorComponent
                | ApiV1DomainsDnszonesUpdateDnssecCryptokeysErrorComponent
                | ApiV1DomainsDnszonesUpdateDnssecDsRecordsErrorComponent
                | ApiV1DomainsDnszonesUpdateDnssecEnabledErrorComponent
                | ApiV1DomainsDnszonesUpdateDnssecNsec3ErrorComponent
                | ApiV1DomainsDnszonesUpdateDsDelegationSyncedErrorComponent
                | ApiV1DomainsDnszonesUpdateKindErrorComponent
                | ApiV1DomainsDnszonesUpdateLabelsErrorComponent
                | ApiV1DomainsDnszonesUpdateLastReconciliationDurationSecondsErrorComponent
                | ApiV1DomainsDnszonesUpdateManagedByContentTypeErrorComponent
                | ApiV1DomainsDnszonesUpdateManagedByObjectIdErrorComponent
                | ApiV1DomainsDnszonesUpdateModifiedByUserErrorComponent
                | ApiV1DomainsDnszonesUpdateNameErrorComponent
                | ApiV1DomainsDnszonesUpdateNonFieldErrorsErrorComponent
                | ApiV1DomainsDnszonesUpdateNsDelegationSyncedErrorComponent
                | ApiV1DomainsDnszonesUpdateOrganizationIdErrorComponent
                | ApiV1DomainsDnszonesUpdatePlatformDnsRecordCreatedErrorComponent
                | ApiV1DomainsDnszonesUpdatePlatformServiceErrorComponent
                | ApiV1DomainsDnszonesUpdatePowerdnsMetadataErrorComponent
                | ApiV1DomainsDnszonesUpdatePrimaryZoneErrorComponent
                | ApiV1DomainsDnszonesUpdateProviderErrorComponent
                | ApiV1DomainsDnszonesUpdateProviderIdErrorComponent
                | ApiV1DomainsDnszonesUpdateProviderReferenceErrorComponent
                | ApiV1DomainsDnszonesUpdateReconciliationEnabledErrorComponent
                | ApiV1DomainsDnszonesUpdateSlaAvailabilityErrorComponent
                | ApiV1DomainsDnszonesUpdateSlaTargetErrorComponent
                | ApiV1DomainsDnszonesUpdateSlaWindowDaysErrorComponent
                | ApiV1DomainsDnszonesUpdateSloAvailabilityErrorComponent
                | ApiV1DomainsDnszonesUpdateSloTargetErrorComponent
                | ApiV1DomainsDnszonesUpdateSloWindowDaysErrorComponent
                | ApiV1DomainsDnszonesUpdateSyncFromErrorComponent
                | ApiV1DomainsDnszonesUpdateTargetAvailabilityErrorComponent
                | ApiV1DomainsDnszonesUpdateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_update_error_type_0 = (
                        ApiV1DomainsDnszonesUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_update_error_type_1 = (
                        ApiV1DomainsDnszonesUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_update_error_type_2 = (
                        ApiV1DomainsDnszonesUpdateCredentialIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_update_error_type_3 = (
                        ApiV1DomainsDnszonesUpdateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_update_error_type_4 = (
                        ApiV1DomainsDnszonesUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_update_error_type_5 = (
                        ApiV1DomainsDnszonesUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_update_error_type_6 = (
                        ApiV1DomainsDnszonesUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_update_error_type_7 = (
                        ApiV1DomainsDnszonesUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_update_error_type_8 = (
                        ApiV1DomainsDnszonesUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_update_error_type_9 = (
                        ApiV1DomainsDnszonesUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_update_error_type_10 = (
                        ApiV1DomainsDnszonesUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_update_error_type_11 = (
                        ApiV1DomainsDnszonesUpdateLastReconciliationDurationSecondsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_update_error_type_12 = (
                        ApiV1DomainsDnszonesUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_update_error_type_13 = (
                        ApiV1DomainsDnszonesUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_update_error_type_14 = (
                        ApiV1DomainsDnszonesUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_update_error_type_15 = (
                        ApiV1DomainsDnszonesUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_update_error_type_16 = (
                        ApiV1DomainsDnszonesUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_update_error_type_17 = (
                        ApiV1DomainsDnszonesUpdateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_update_error_type_18 = (
                        ApiV1DomainsDnszonesUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_update_error_type_19 = (
                        ApiV1DomainsDnszonesUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_update_error_type_20 = (
                        ApiV1DomainsDnszonesUpdateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_update_error_type_21 = (
                        ApiV1DomainsDnszonesUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_update_error_type_22 = (
                        ApiV1DomainsDnszonesUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_update_error_type_23 = (
                        ApiV1DomainsDnszonesUpdateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_update_error_type_24 = (
                        ApiV1DomainsDnszonesUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_update_error_type_25 = (
                        ApiV1DomainsDnszonesUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_update_error_type_26 = (
                        ApiV1DomainsDnszonesUpdateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_update_error_type_27 = (
                        ApiV1DomainsDnszonesUpdatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_update_error_type_28 = (
                        ApiV1DomainsDnszonesUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_update_error_type_29 = (
                        ApiV1DomainsDnszonesUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_update_error_type_30 = (
                        ApiV1DomainsDnszonesUpdatePrimaryZoneErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_update_error_type_31 = (
                        ApiV1DomainsDnszonesUpdatePowerdnsMetadataErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_update_error_type_32 = (
                        ApiV1DomainsDnszonesUpdateDefaultTtlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_update_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_update_error_type_33 = (
                        ApiV1DomainsDnszonesUpdateDnssecEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_update_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_update_error_type_34 = (
                        ApiV1DomainsDnszonesUpdateDnssecAlgorithmErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_update_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_update_error_type_35 = (
                        ApiV1DomainsDnszonesUpdateDnssecNsec3ErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_update_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_update_error_type_36 = (
                        ApiV1DomainsDnszonesUpdateDnssecDsRecordsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_update_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_update_error_type_37 = (
                        ApiV1DomainsDnszonesUpdateDnssecCryptokeysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_update_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_update_error_type_38 = (
                        ApiV1DomainsDnszonesUpdateNsDelegationSyncedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_update_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_update_error_type_39 = (
                        ApiV1DomainsDnszonesUpdateDsDelegationSyncedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_update_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_update_error_type_40 = (
                        ApiV1DomainsDnszonesUpdateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_update_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_update_error_type_41 = (
                        ApiV1DomainsDnszonesUpdateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_update_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_update_error_type_42 = (
                        ApiV1DomainsDnszonesUpdateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_update_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_update_error_type_43 = (
                        ApiV1DomainsDnszonesUpdateCreatedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_update_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_domains_dnszones_update_error_type_44 = (
                    ApiV1DomainsDnszonesUpdateSyncFromErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_domains_dnszones_update_error_type_44

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_domains_dnszones_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_domains_dnszones_update_validation_error.additional_properties = d
        return api_v1_domains_dnszones_update_validation_error

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
