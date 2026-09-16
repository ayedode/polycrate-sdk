from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_domains_dnszones_partial_update_annotations_error_component import (
        ApiV1DomainsDnszonesPartialUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_partial_update_archived_at_error_component import (
        ApiV1DomainsDnszonesPartialUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_partial_update_archived_by_error_component import (
        ApiV1DomainsDnszonesPartialUpdateArchivedByErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_partial_update_archived_error_component import (
        ApiV1DomainsDnszonesPartialUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_partial_update_archived_reason_error_component import (
        ApiV1DomainsDnszonesPartialUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_partial_update_created_by_component_error_component import (
        ApiV1DomainsDnszonesPartialUpdateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_partial_update_created_by_user_error_component import (
        ApiV1DomainsDnszonesPartialUpdateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_partial_update_credential_id_error_component import (
        ApiV1DomainsDnszonesPartialUpdateCredentialIdErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_partial_update_criticality_error_component import (
        ApiV1DomainsDnszonesPartialUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_partial_update_debug_mode_error_component import (
        ApiV1DomainsDnszonesPartialUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_partial_update_default_ttl_error_component import (
        ApiV1DomainsDnszonesPartialUpdateDefaultTtlErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_partial_update_display_name_error_component import (
        ApiV1DomainsDnszonesPartialUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_partial_update_dnssec_algorithm_error_component import (
        ApiV1DomainsDnszonesPartialUpdateDnssecAlgorithmErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_partial_update_dnssec_cryptokeys_error_component import (
        ApiV1DomainsDnszonesPartialUpdateDnssecCryptokeysErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_partial_update_dnssec_ds_records_error_component import (
        ApiV1DomainsDnszonesPartialUpdateDnssecDsRecordsErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_partial_update_dnssec_enabled_error_component import (
        ApiV1DomainsDnszonesPartialUpdateDnssecEnabledErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_partial_update_dnssec_nsec_3_error_component import (
        ApiV1DomainsDnszonesPartialUpdateDnssecNsec3ErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_partial_update_ds_delegation_synced_error_component import (
        ApiV1DomainsDnszonesPartialUpdateDsDelegationSyncedErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_partial_update_kind_error_component import (
        ApiV1DomainsDnszonesPartialUpdateKindErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_partial_update_labels_error_component import (
        ApiV1DomainsDnszonesPartialUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_partial_update_last_reconciliation_duration_seconds_error_component import (
        ApiV1DomainsDnszonesPartialUpdateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_partial_update_managed_by_content_type_error_component import (
        ApiV1DomainsDnszonesPartialUpdateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_partial_update_managed_by_object_id_error_component import (
        ApiV1DomainsDnszonesPartialUpdateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_partial_update_modified_by_user_error_component import (
        ApiV1DomainsDnszonesPartialUpdateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_partial_update_name_error_component import (
        ApiV1DomainsDnszonesPartialUpdateNameErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_partial_update_non_field_errors_error_component import (
        ApiV1DomainsDnszonesPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_partial_update_ns_delegation_synced_error_component import (
        ApiV1DomainsDnszonesPartialUpdateNsDelegationSyncedErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_partial_update_organization_id_error_component import (
        ApiV1DomainsDnszonesPartialUpdateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_partial_update_platform_dns_record_created_error_component import (
        ApiV1DomainsDnszonesPartialUpdatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_partial_update_platform_service_error_component import (
        ApiV1DomainsDnszonesPartialUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_partial_update_powerdns_metadata_error_component import (
        ApiV1DomainsDnszonesPartialUpdatePowerdnsMetadataErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_partial_update_primary_zone_error_component import (
        ApiV1DomainsDnszonesPartialUpdatePrimaryZoneErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_partial_update_provider_error_component import (
        ApiV1DomainsDnszonesPartialUpdateProviderErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_partial_update_provider_id_error_component import (
        ApiV1DomainsDnszonesPartialUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_partial_update_provider_reference_error_component import (
        ApiV1DomainsDnszonesPartialUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_partial_update_reconciliation_enabled_error_component import (
        ApiV1DomainsDnszonesPartialUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_partial_update_sla_availability_error_component import (
        ApiV1DomainsDnszonesPartialUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_partial_update_sla_target_error_component import (
        ApiV1DomainsDnszonesPartialUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_partial_update_sla_window_days_error_component import (
        ApiV1DomainsDnszonesPartialUpdateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_partial_update_slo_availability_error_component import (
        ApiV1DomainsDnszonesPartialUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_partial_update_slo_target_error_component import (
        ApiV1DomainsDnszonesPartialUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_partial_update_slo_window_days_error_component import (
        ApiV1DomainsDnszonesPartialUpdateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_partial_update_sync_from_error_component import (
        ApiV1DomainsDnszonesPartialUpdateSyncFromErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_partial_update_target_availability_error_component import (
        ApiV1DomainsDnszonesPartialUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_partial_update_tolerations_error_component import (
        ApiV1DomainsDnszonesPartialUpdateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1DomainsDnszonesPartialUpdateValidationError")


@_attrs_define
class ApiV1DomainsDnszonesPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1DomainsDnszonesPartialUpdateAnnotationsErrorComponent |
            ApiV1DomainsDnszonesPartialUpdateArchivedAtErrorComponent |
            ApiV1DomainsDnszonesPartialUpdateArchivedByErrorComponent |
            ApiV1DomainsDnszonesPartialUpdateArchivedErrorComponent |
            ApiV1DomainsDnszonesPartialUpdateArchivedReasonErrorComponent |
            ApiV1DomainsDnszonesPartialUpdateCreatedByComponentErrorComponent |
            ApiV1DomainsDnszonesPartialUpdateCreatedByUserErrorComponent |
            ApiV1DomainsDnszonesPartialUpdateCredentialIdErrorComponent |
            ApiV1DomainsDnszonesPartialUpdateCriticalityErrorComponent |
            ApiV1DomainsDnszonesPartialUpdateDebugModeErrorComponent |
            ApiV1DomainsDnszonesPartialUpdateDefaultTtlErrorComponent |
            ApiV1DomainsDnszonesPartialUpdateDisplayNameErrorComponent |
            ApiV1DomainsDnszonesPartialUpdateDnssecAlgorithmErrorComponent |
            ApiV1DomainsDnszonesPartialUpdateDnssecCryptokeysErrorComponent |
            ApiV1DomainsDnszonesPartialUpdateDnssecDsRecordsErrorComponent |
            ApiV1DomainsDnszonesPartialUpdateDnssecEnabledErrorComponent |
            ApiV1DomainsDnszonesPartialUpdateDnssecNsec3ErrorComponent |
            ApiV1DomainsDnszonesPartialUpdateDsDelegationSyncedErrorComponent |
            ApiV1DomainsDnszonesPartialUpdateKindErrorComponent | ApiV1DomainsDnszonesPartialUpdateLabelsErrorComponent |
            ApiV1DomainsDnszonesPartialUpdateLastReconciliationDurationSecondsErrorComponent |
            ApiV1DomainsDnszonesPartialUpdateManagedByContentTypeErrorComponent |
            ApiV1DomainsDnszonesPartialUpdateManagedByObjectIdErrorComponent |
            ApiV1DomainsDnszonesPartialUpdateModifiedByUserErrorComponent |
            ApiV1DomainsDnszonesPartialUpdateNameErrorComponent |
            ApiV1DomainsDnszonesPartialUpdateNonFieldErrorsErrorComponent |
            ApiV1DomainsDnszonesPartialUpdateNsDelegationSyncedErrorComponent |
            ApiV1DomainsDnszonesPartialUpdateOrganizationIdErrorComponent |
            ApiV1DomainsDnszonesPartialUpdatePlatformDnsRecordCreatedErrorComponent |
            ApiV1DomainsDnszonesPartialUpdatePlatformServiceErrorComponent |
            ApiV1DomainsDnszonesPartialUpdatePowerdnsMetadataErrorComponent |
            ApiV1DomainsDnszonesPartialUpdatePrimaryZoneErrorComponent |
            ApiV1DomainsDnszonesPartialUpdateProviderErrorComponent |
            ApiV1DomainsDnszonesPartialUpdateProviderIdErrorComponent |
            ApiV1DomainsDnszonesPartialUpdateProviderReferenceErrorComponent |
            ApiV1DomainsDnszonesPartialUpdateReconciliationEnabledErrorComponent |
            ApiV1DomainsDnszonesPartialUpdateSlaAvailabilityErrorComponent |
            ApiV1DomainsDnszonesPartialUpdateSlaTargetErrorComponent |
            ApiV1DomainsDnszonesPartialUpdateSlaWindowDaysErrorComponent |
            ApiV1DomainsDnszonesPartialUpdateSloAvailabilityErrorComponent |
            ApiV1DomainsDnszonesPartialUpdateSloTargetErrorComponent |
            ApiV1DomainsDnszonesPartialUpdateSloWindowDaysErrorComponent |
            ApiV1DomainsDnszonesPartialUpdateSyncFromErrorComponent |
            ApiV1DomainsDnszonesPartialUpdateTargetAvailabilityErrorComponent |
            ApiV1DomainsDnszonesPartialUpdateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1DomainsDnszonesPartialUpdateAnnotationsErrorComponent
        | ApiV1DomainsDnszonesPartialUpdateArchivedAtErrorComponent
        | ApiV1DomainsDnszonesPartialUpdateArchivedByErrorComponent
        | ApiV1DomainsDnszonesPartialUpdateArchivedErrorComponent
        | ApiV1DomainsDnszonesPartialUpdateArchivedReasonErrorComponent
        | ApiV1DomainsDnszonesPartialUpdateCreatedByComponentErrorComponent
        | ApiV1DomainsDnszonesPartialUpdateCreatedByUserErrorComponent
        | ApiV1DomainsDnszonesPartialUpdateCredentialIdErrorComponent
        | ApiV1DomainsDnszonesPartialUpdateCriticalityErrorComponent
        | ApiV1DomainsDnszonesPartialUpdateDebugModeErrorComponent
        | ApiV1DomainsDnszonesPartialUpdateDefaultTtlErrorComponent
        | ApiV1DomainsDnszonesPartialUpdateDisplayNameErrorComponent
        | ApiV1DomainsDnszonesPartialUpdateDnssecAlgorithmErrorComponent
        | ApiV1DomainsDnszonesPartialUpdateDnssecCryptokeysErrorComponent
        | ApiV1DomainsDnszonesPartialUpdateDnssecDsRecordsErrorComponent
        | ApiV1DomainsDnszonesPartialUpdateDnssecEnabledErrorComponent
        | ApiV1DomainsDnszonesPartialUpdateDnssecNsec3ErrorComponent
        | ApiV1DomainsDnszonesPartialUpdateDsDelegationSyncedErrorComponent
        | ApiV1DomainsDnszonesPartialUpdateKindErrorComponent
        | ApiV1DomainsDnszonesPartialUpdateLabelsErrorComponent
        | ApiV1DomainsDnszonesPartialUpdateLastReconciliationDurationSecondsErrorComponent
        | ApiV1DomainsDnszonesPartialUpdateManagedByContentTypeErrorComponent
        | ApiV1DomainsDnszonesPartialUpdateManagedByObjectIdErrorComponent
        | ApiV1DomainsDnszonesPartialUpdateModifiedByUserErrorComponent
        | ApiV1DomainsDnszonesPartialUpdateNameErrorComponent
        | ApiV1DomainsDnszonesPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1DomainsDnszonesPartialUpdateNsDelegationSyncedErrorComponent
        | ApiV1DomainsDnszonesPartialUpdateOrganizationIdErrorComponent
        | ApiV1DomainsDnszonesPartialUpdatePlatformDnsRecordCreatedErrorComponent
        | ApiV1DomainsDnszonesPartialUpdatePlatformServiceErrorComponent
        | ApiV1DomainsDnszonesPartialUpdatePowerdnsMetadataErrorComponent
        | ApiV1DomainsDnszonesPartialUpdatePrimaryZoneErrorComponent
        | ApiV1DomainsDnszonesPartialUpdateProviderErrorComponent
        | ApiV1DomainsDnszonesPartialUpdateProviderIdErrorComponent
        | ApiV1DomainsDnszonesPartialUpdateProviderReferenceErrorComponent
        | ApiV1DomainsDnszonesPartialUpdateReconciliationEnabledErrorComponent
        | ApiV1DomainsDnszonesPartialUpdateSlaAvailabilityErrorComponent
        | ApiV1DomainsDnszonesPartialUpdateSlaTargetErrorComponent
        | ApiV1DomainsDnszonesPartialUpdateSlaWindowDaysErrorComponent
        | ApiV1DomainsDnszonesPartialUpdateSloAvailabilityErrorComponent
        | ApiV1DomainsDnszonesPartialUpdateSloTargetErrorComponent
        | ApiV1DomainsDnszonesPartialUpdateSloWindowDaysErrorComponent
        | ApiV1DomainsDnszonesPartialUpdateSyncFromErrorComponent
        | ApiV1DomainsDnszonesPartialUpdateTargetAvailabilityErrorComponent
        | ApiV1DomainsDnszonesPartialUpdateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_domains_dnszones_partial_update_annotations_error_component import (
            ApiV1DomainsDnszonesPartialUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_archived_at_error_component import (
            ApiV1DomainsDnszonesPartialUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_archived_by_error_component import (
            ApiV1DomainsDnszonesPartialUpdateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_archived_error_component import (
            ApiV1DomainsDnszonesPartialUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_archived_reason_error_component import (
            ApiV1DomainsDnszonesPartialUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_created_by_component_error_component import (
            ApiV1DomainsDnszonesPartialUpdateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_created_by_user_error_component import (
            ApiV1DomainsDnszonesPartialUpdateCreatedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_credential_id_error_component import (
            ApiV1DomainsDnszonesPartialUpdateCredentialIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_criticality_error_component import (
            ApiV1DomainsDnszonesPartialUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_debug_mode_error_component import (
            ApiV1DomainsDnszonesPartialUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_default_ttl_error_component import (
            ApiV1DomainsDnszonesPartialUpdateDefaultTtlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_display_name_error_component import (
            ApiV1DomainsDnszonesPartialUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_dnssec_algorithm_error_component import (
            ApiV1DomainsDnszonesPartialUpdateDnssecAlgorithmErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_dnssec_cryptokeys_error_component import (
            ApiV1DomainsDnszonesPartialUpdateDnssecCryptokeysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_dnssec_ds_records_error_component import (
            ApiV1DomainsDnszonesPartialUpdateDnssecDsRecordsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_dnssec_enabled_error_component import (
            ApiV1DomainsDnszonesPartialUpdateDnssecEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_dnssec_nsec_3_error_component import (
            ApiV1DomainsDnszonesPartialUpdateDnssecNsec3ErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_ds_delegation_synced_error_component import (
            ApiV1DomainsDnszonesPartialUpdateDsDelegationSyncedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_kind_error_component import (
            ApiV1DomainsDnszonesPartialUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_labels_error_component import (
            ApiV1DomainsDnszonesPartialUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_last_reconciliation_duration_seconds_error_component import (
            ApiV1DomainsDnszonesPartialUpdateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_managed_by_content_type_error_component import (
            ApiV1DomainsDnszonesPartialUpdateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_managed_by_object_id_error_component import (
            ApiV1DomainsDnszonesPartialUpdateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_modified_by_user_error_component import (
            ApiV1DomainsDnszonesPartialUpdateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_name_error_component import (
            ApiV1DomainsDnszonesPartialUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_non_field_errors_error_component import (
            ApiV1DomainsDnszonesPartialUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_ns_delegation_synced_error_component import (
            ApiV1DomainsDnszonesPartialUpdateNsDelegationSyncedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_organization_id_error_component import (
            ApiV1DomainsDnszonesPartialUpdateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_platform_dns_record_created_error_component import (
            ApiV1DomainsDnszonesPartialUpdatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_platform_service_error_component import (
            ApiV1DomainsDnszonesPartialUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_powerdns_metadata_error_component import (
            ApiV1DomainsDnszonesPartialUpdatePowerdnsMetadataErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_primary_zone_error_component import (
            ApiV1DomainsDnszonesPartialUpdatePrimaryZoneErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_provider_error_component import (
            ApiV1DomainsDnszonesPartialUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_provider_id_error_component import (
            ApiV1DomainsDnszonesPartialUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_provider_reference_error_component import (
            ApiV1DomainsDnszonesPartialUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_reconciliation_enabled_error_component import (
            ApiV1DomainsDnszonesPartialUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_sla_availability_error_component import (
            ApiV1DomainsDnszonesPartialUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_sla_target_error_component import (
            ApiV1DomainsDnszonesPartialUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_sla_window_days_error_component import (
            ApiV1DomainsDnszonesPartialUpdateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_slo_availability_error_component import (
            ApiV1DomainsDnszonesPartialUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_slo_target_error_component import (
            ApiV1DomainsDnszonesPartialUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_slo_window_days_error_component import (
            ApiV1DomainsDnszonesPartialUpdateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_target_availability_error_component import (
            ApiV1DomainsDnszonesPartialUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_tolerations_error_component import (
            ApiV1DomainsDnszonesPartialUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1DomainsDnszonesPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesPartialUpdateCredentialIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesPartialUpdateOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesPartialUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesPartialUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesPartialUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesPartialUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesPartialUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesPartialUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesPartialUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1DomainsDnszonesPartialUpdateLastReconciliationDurationSecondsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesPartialUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesPartialUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesPartialUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesPartialUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesPartialUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesPartialUpdateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesPartialUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesPartialUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesPartialUpdateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesPartialUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesPartialUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesPartialUpdateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesPartialUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesPartialUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesPartialUpdateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesPartialUpdatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesPartialUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesPartialUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesPartialUpdatePrimaryZoneErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesPartialUpdatePowerdnsMetadataErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesPartialUpdateDefaultTtlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesPartialUpdateDnssecEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesPartialUpdateDnssecAlgorithmErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesPartialUpdateDnssecNsec3ErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesPartialUpdateDnssecDsRecordsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesPartialUpdateDnssecCryptokeysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesPartialUpdateNsDelegationSyncedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesPartialUpdateDsDelegationSyncedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesPartialUpdateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesPartialUpdateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesPartialUpdateModifiedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesPartialUpdateCreatedByUserErrorComponent):
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
        from ..models.api_v1_domains_dnszones_partial_update_annotations_error_component import (
            ApiV1DomainsDnszonesPartialUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_archived_at_error_component import (
            ApiV1DomainsDnszonesPartialUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_archived_by_error_component import (
            ApiV1DomainsDnszonesPartialUpdateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_archived_error_component import (
            ApiV1DomainsDnszonesPartialUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_archived_reason_error_component import (
            ApiV1DomainsDnszonesPartialUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_created_by_component_error_component import (
            ApiV1DomainsDnszonesPartialUpdateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_created_by_user_error_component import (
            ApiV1DomainsDnszonesPartialUpdateCreatedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_credential_id_error_component import (
            ApiV1DomainsDnszonesPartialUpdateCredentialIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_criticality_error_component import (
            ApiV1DomainsDnszonesPartialUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_debug_mode_error_component import (
            ApiV1DomainsDnszonesPartialUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_default_ttl_error_component import (
            ApiV1DomainsDnszonesPartialUpdateDefaultTtlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_display_name_error_component import (
            ApiV1DomainsDnszonesPartialUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_dnssec_algorithm_error_component import (
            ApiV1DomainsDnszonesPartialUpdateDnssecAlgorithmErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_dnssec_cryptokeys_error_component import (
            ApiV1DomainsDnszonesPartialUpdateDnssecCryptokeysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_dnssec_ds_records_error_component import (
            ApiV1DomainsDnszonesPartialUpdateDnssecDsRecordsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_dnssec_enabled_error_component import (
            ApiV1DomainsDnszonesPartialUpdateDnssecEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_dnssec_nsec_3_error_component import (
            ApiV1DomainsDnszonesPartialUpdateDnssecNsec3ErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_ds_delegation_synced_error_component import (
            ApiV1DomainsDnszonesPartialUpdateDsDelegationSyncedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_kind_error_component import (
            ApiV1DomainsDnszonesPartialUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_labels_error_component import (
            ApiV1DomainsDnszonesPartialUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_last_reconciliation_duration_seconds_error_component import (
            ApiV1DomainsDnszonesPartialUpdateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_managed_by_content_type_error_component import (
            ApiV1DomainsDnszonesPartialUpdateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_managed_by_object_id_error_component import (
            ApiV1DomainsDnszonesPartialUpdateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_modified_by_user_error_component import (
            ApiV1DomainsDnszonesPartialUpdateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_name_error_component import (
            ApiV1DomainsDnszonesPartialUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_non_field_errors_error_component import (
            ApiV1DomainsDnszonesPartialUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_ns_delegation_synced_error_component import (
            ApiV1DomainsDnszonesPartialUpdateNsDelegationSyncedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_organization_id_error_component import (
            ApiV1DomainsDnszonesPartialUpdateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_platform_dns_record_created_error_component import (
            ApiV1DomainsDnszonesPartialUpdatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_platform_service_error_component import (
            ApiV1DomainsDnszonesPartialUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_powerdns_metadata_error_component import (
            ApiV1DomainsDnszonesPartialUpdatePowerdnsMetadataErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_primary_zone_error_component import (
            ApiV1DomainsDnszonesPartialUpdatePrimaryZoneErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_provider_error_component import (
            ApiV1DomainsDnszonesPartialUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_provider_id_error_component import (
            ApiV1DomainsDnszonesPartialUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_provider_reference_error_component import (
            ApiV1DomainsDnszonesPartialUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_reconciliation_enabled_error_component import (
            ApiV1DomainsDnszonesPartialUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_sla_availability_error_component import (
            ApiV1DomainsDnszonesPartialUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_sla_target_error_component import (
            ApiV1DomainsDnszonesPartialUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_sla_window_days_error_component import (
            ApiV1DomainsDnszonesPartialUpdateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_slo_availability_error_component import (
            ApiV1DomainsDnszonesPartialUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_slo_target_error_component import (
            ApiV1DomainsDnszonesPartialUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_slo_window_days_error_component import (
            ApiV1DomainsDnszonesPartialUpdateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_sync_from_error_component import (
            ApiV1DomainsDnszonesPartialUpdateSyncFromErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_target_availability_error_component import (
            ApiV1DomainsDnszonesPartialUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_partial_update_tolerations_error_component import (
            ApiV1DomainsDnszonesPartialUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1DomainsDnszonesPartialUpdateAnnotationsErrorComponent
                | ApiV1DomainsDnszonesPartialUpdateArchivedAtErrorComponent
                | ApiV1DomainsDnszonesPartialUpdateArchivedByErrorComponent
                | ApiV1DomainsDnszonesPartialUpdateArchivedErrorComponent
                | ApiV1DomainsDnszonesPartialUpdateArchivedReasonErrorComponent
                | ApiV1DomainsDnszonesPartialUpdateCreatedByComponentErrorComponent
                | ApiV1DomainsDnszonesPartialUpdateCreatedByUserErrorComponent
                | ApiV1DomainsDnszonesPartialUpdateCredentialIdErrorComponent
                | ApiV1DomainsDnszonesPartialUpdateCriticalityErrorComponent
                | ApiV1DomainsDnszonesPartialUpdateDebugModeErrorComponent
                | ApiV1DomainsDnszonesPartialUpdateDefaultTtlErrorComponent
                | ApiV1DomainsDnszonesPartialUpdateDisplayNameErrorComponent
                | ApiV1DomainsDnszonesPartialUpdateDnssecAlgorithmErrorComponent
                | ApiV1DomainsDnszonesPartialUpdateDnssecCryptokeysErrorComponent
                | ApiV1DomainsDnszonesPartialUpdateDnssecDsRecordsErrorComponent
                | ApiV1DomainsDnszonesPartialUpdateDnssecEnabledErrorComponent
                | ApiV1DomainsDnszonesPartialUpdateDnssecNsec3ErrorComponent
                | ApiV1DomainsDnszonesPartialUpdateDsDelegationSyncedErrorComponent
                | ApiV1DomainsDnszonesPartialUpdateKindErrorComponent
                | ApiV1DomainsDnszonesPartialUpdateLabelsErrorComponent
                | ApiV1DomainsDnszonesPartialUpdateLastReconciliationDurationSecondsErrorComponent
                | ApiV1DomainsDnszonesPartialUpdateManagedByContentTypeErrorComponent
                | ApiV1DomainsDnszonesPartialUpdateManagedByObjectIdErrorComponent
                | ApiV1DomainsDnszonesPartialUpdateModifiedByUserErrorComponent
                | ApiV1DomainsDnszonesPartialUpdateNameErrorComponent
                | ApiV1DomainsDnszonesPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1DomainsDnszonesPartialUpdateNsDelegationSyncedErrorComponent
                | ApiV1DomainsDnszonesPartialUpdateOrganizationIdErrorComponent
                | ApiV1DomainsDnszonesPartialUpdatePlatformDnsRecordCreatedErrorComponent
                | ApiV1DomainsDnszonesPartialUpdatePlatformServiceErrorComponent
                | ApiV1DomainsDnszonesPartialUpdatePowerdnsMetadataErrorComponent
                | ApiV1DomainsDnszonesPartialUpdatePrimaryZoneErrorComponent
                | ApiV1DomainsDnszonesPartialUpdateProviderErrorComponent
                | ApiV1DomainsDnszonesPartialUpdateProviderIdErrorComponent
                | ApiV1DomainsDnszonesPartialUpdateProviderReferenceErrorComponent
                | ApiV1DomainsDnszonesPartialUpdateReconciliationEnabledErrorComponent
                | ApiV1DomainsDnszonesPartialUpdateSlaAvailabilityErrorComponent
                | ApiV1DomainsDnszonesPartialUpdateSlaTargetErrorComponent
                | ApiV1DomainsDnszonesPartialUpdateSlaWindowDaysErrorComponent
                | ApiV1DomainsDnszonesPartialUpdateSloAvailabilityErrorComponent
                | ApiV1DomainsDnszonesPartialUpdateSloTargetErrorComponent
                | ApiV1DomainsDnszonesPartialUpdateSloWindowDaysErrorComponent
                | ApiV1DomainsDnszonesPartialUpdateSyncFromErrorComponent
                | ApiV1DomainsDnszonesPartialUpdateTargetAvailabilityErrorComponent
                | ApiV1DomainsDnszonesPartialUpdateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_partial_update_error_type_0 = (
                        ApiV1DomainsDnszonesPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_partial_update_error_type_1 = (
                        ApiV1DomainsDnszonesPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_partial_update_error_type_2 = (
                        ApiV1DomainsDnszonesPartialUpdateCredentialIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_partial_update_error_type_3 = (
                        ApiV1DomainsDnszonesPartialUpdateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_partial_update_error_type_4 = (
                        ApiV1DomainsDnszonesPartialUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_partial_update_error_type_5 = (
                        ApiV1DomainsDnszonesPartialUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_partial_update_error_type_6 = (
                        ApiV1DomainsDnszonesPartialUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_partial_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_partial_update_error_type_7 = (
                        ApiV1DomainsDnszonesPartialUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_partial_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_partial_update_error_type_8 = (
                        ApiV1DomainsDnszonesPartialUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_partial_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_partial_update_error_type_9 = (
                        ApiV1DomainsDnszonesPartialUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_partial_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_partial_update_error_type_10 = (
                        ApiV1DomainsDnszonesPartialUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_partial_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_partial_update_error_type_11 = (
                        ApiV1DomainsDnszonesPartialUpdateLastReconciliationDurationSecondsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_partial_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_partial_update_error_type_12 = (
                        ApiV1DomainsDnszonesPartialUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_partial_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_partial_update_error_type_13 = (
                        ApiV1DomainsDnszonesPartialUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_partial_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_partial_update_error_type_14 = (
                        ApiV1DomainsDnszonesPartialUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_partial_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_partial_update_error_type_15 = (
                        ApiV1DomainsDnszonesPartialUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_partial_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_partial_update_error_type_16 = (
                        ApiV1DomainsDnszonesPartialUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_partial_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_partial_update_error_type_17 = (
                        ApiV1DomainsDnszonesPartialUpdateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_partial_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_partial_update_error_type_18 = (
                        ApiV1DomainsDnszonesPartialUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_partial_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_partial_update_error_type_19 = (
                        ApiV1DomainsDnszonesPartialUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_partial_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_partial_update_error_type_20 = (
                        ApiV1DomainsDnszonesPartialUpdateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_partial_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_partial_update_error_type_21 = (
                        ApiV1DomainsDnszonesPartialUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_partial_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_partial_update_error_type_22 = (
                        ApiV1DomainsDnszonesPartialUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_partial_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_partial_update_error_type_23 = (
                        ApiV1DomainsDnszonesPartialUpdateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_partial_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_partial_update_error_type_24 = (
                        ApiV1DomainsDnszonesPartialUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_partial_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_partial_update_error_type_25 = (
                        ApiV1DomainsDnszonesPartialUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_partial_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_partial_update_error_type_26 = (
                        ApiV1DomainsDnszonesPartialUpdateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_partial_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_partial_update_error_type_27 = (
                        ApiV1DomainsDnszonesPartialUpdatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_partial_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_partial_update_error_type_28 = (
                        ApiV1DomainsDnszonesPartialUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_partial_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_partial_update_error_type_29 = (
                        ApiV1DomainsDnszonesPartialUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_partial_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_partial_update_error_type_30 = (
                        ApiV1DomainsDnszonesPartialUpdatePrimaryZoneErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_partial_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_partial_update_error_type_31 = (
                        ApiV1DomainsDnszonesPartialUpdatePowerdnsMetadataErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_partial_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_partial_update_error_type_32 = (
                        ApiV1DomainsDnszonesPartialUpdateDefaultTtlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_partial_update_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_partial_update_error_type_33 = (
                        ApiV1DomainsDnszonesPartialUpdateDnssecEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_partial_update_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_partial_update_error_type_34 = (
                        ApiV1DomainsDnszonesPartialUpdateDnssecAlgorithmErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_partial_update_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_partial_update_error_type_35 = (
                        ApiV1DomainsDnszonesPartialUpdateDnssecNsec3ErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_partial_update_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_partial_update_error_type_36 = (
                        ApiV1DomainsDnszonesPartialUpdateDnssecDsRecordsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_partial_update_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_partial_update_error_type_37 = (
                        ApiV1DomainsDnszonesPartialUpdateDnssecCryptokeysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_partial_update_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_partial_update_error_type_38 = (
                        ApiV1DomainsDnszonesPartialUpdateNsDelegationSyncedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_partial_update_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_partial_update_error_type_39 = (
                        ApiV1DomainsDnszonesPartialUpdateDsDelegationSyncedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_partial_update_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_partial_update_error_type_40 = (
                        ApiV1DomainsDnszonesPartialUpdateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_partial_update_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_partial_update_error_type_41 = (
                        ApiV1DomainsDnszonesPartialUpdateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_partial_update_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_partial_update_error_type_42 = (
                        ApiV1DomainsDnszonesPartialUpdateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_partial_update_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_partial_update_error_type_43 = (
                        ApiV1DomainsDnszonesPartialUpdateCreatedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_partial_update_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_domains_dnszones_partial_update_error_type_44 = (
                    ApiV1DomainsDnszonesPartialUpdateSyncFromErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_domains_dnszones_partial_update_error_type_44

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_domains_dnszones_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_domains_dnszones_partial_update_validation_error.additional_properties = d
        return api_v1_domains_dnszones_partial_update_validation_error

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
