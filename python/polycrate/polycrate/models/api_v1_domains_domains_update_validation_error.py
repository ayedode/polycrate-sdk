from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_domains_domains_update_admin_contact_id_error_component import (
        ApiV1DomainsDomainsUpdateAdminContactIdErrorComponent,
    )
    from ..models.api_v1_domains_domains_update_annotations_error_component import (
        ApiV1DomainsDomainsUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_domains_domains_update_archived_at_error_component import (
        ApiV1DomainsDomainsUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_domains_domains_update_archived_by_error_component import (
        ApiV1DomainsDomainsUpdateArchivedByErrorComponent,
    )
    from ..models.api_v1_domains_domains_update_archived_error_component import (
        ApiV1DomainsDomainsUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_domains_domains_update_archived_reason_error_component import (
        ApiV1DomainsDomainsUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_domains_domains_update_auth_code_credential_id_error_component import (
        ApiV1DomainsDomainsUpdateAuthCodeCredentialIdErrorComponent,
    )
    from ..models.api_v1_domains_domains_update_created_by_component_error_component import (
        ApiV1DomainsDomainsUpdateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_domains_domains_update_created_by_user_error_component import (
        ApiV1DomainsDomainsUpdateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_domains_domains_update_criticality_error_component import (
        ApiV1DomainsDomainsUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_domains_domains_update_debug_mode_error_component import (
        ApiV1DomainsDomainsUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_domains_domains_update_display_name_error_component import (
        ApiV1DomainsDomainsUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_domains_domains_update_dns_zone_id_error_component import (
        ApiV1DomainsDomainsUpdateDnsZoneIdErrorComponent,
    )
    from ..models.api_v1_domains_domains_update_expiry_date_error_component import (
        ApiV1DomainsDomainsUpdateExpiryDateErrorComponent,
    )
    from ..models.api_v1_domains_domains_update_kind_error_component import ApiV1DomainsDomainsUpdateKindErrorComponent
    from ..models.api_v1_domains_domains_update_labels_error_component import (
        ApiV1DomainsDomainsUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_domains_domains_update_last_reconciliation_duration_seconds_error_component import (
        ApiV1DomainsDomainsUpdateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_domains_domains_update_managed_by_content_type_error_component import (
        ApiV1DomainsDomainsUpdateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_domains_domains_update_managed_by_object_id_error_component import (
        ApiV1DomainsDomainsUpdateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_domains_domains_update_modified_by_user_error_component import (
        ApiV1DomainsDomainsUpdateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_domains_domains_update_name_error_component import ApiV1DomainsDomainsUpdateNameErrorComponent
    from ..models.api_v1_domains_domains_update_nameservers_error_component import (
        ApiV1DomainsDomainsUpdateNameserversErrorComponent,
    )
    from ..models.api_v1_domains_domains_update_non_field_errors_error_component import (
        ApiV1DomainsDomainsUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_domains_domains_update_owner_contact_id_error_component import (
        ApiV1DomainsDomainsUpdateOwnerContactIdErrorComponent,
    )
    from ..models.api_v1_domains_domains_update_platform_dns_record_created_error_component import (
        ApiV1DomainsDomainsUpdatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_domains_domains_update_platform_service_error_component import (
        ApiV1DomainsDomainsUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_domains_domains_update_provider_error_component import (
        ApiV1DomainsDomainsUpdateProviderErrorComponent,
    )
    from ..models.api_v1_domains_domains_update_provider_id_error_component import (
        ApiV1DomainsDomainsUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_domains_domains_update_provider_reference_error_component import (
        ApiV1DomainsDomainsUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_domains_domains_update_provider_status_error_component import (
        ApiV1DomainsDomainsUpdateProviderStatusErrorComponent,
    )
    from ..models.api_v1_domains_domains_update_reconciliation_enabled_error_component import (
        ApiV1DomainsDomainsUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_domains_domains_update_registrar_domain_id_error_component import (
        ApiV1DomainsDomainsUpdateRegistrarDomainIdErrorComponent,
    )
    from ..models.api_v1_domains_domains_update_registrar_id_error_component import (
        ApiV1DomainsDomainsUpdateRegistrarIdErrorComponent,
    )
    from ..models.api_v1_domains_domains_update_registrar_metadata_error_component import (
        ApiV1DomainsDomainsUpdateRegistrarMetadataErrorComponent,
    )
    from ..models.api_v1_domains_domains_update_renewal_mode_error_component import (
        ApiV1DomainsDomainsUpdateRenewalModeErrorComponent,
    )
    from ..models.api_v1_domains_domains_update_sla_availability_error_component import (
        ApiV1DomainsDomainsUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_domains_domains_update_sla_target_error_component import (
        ApiV1DomainsDomainsUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_domains_domains_update_sla_window_days_error_component import (
        ApiV1DomainsDomainsUpdateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_domains_domains_update_slo_availability_error_component import (
        ApiV1DomainsDomainsUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_domains_domains_update_slo_target_error_component import (
        ApiV1DomainsDomainsUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_domains_domains_update_slo_window_days_error_component import (
        ApiV1DomainsDomainsUpdateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_domains_domains_update_target_availability_error_component import (
        ApiV1DomainsDomainsUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_domains_domains_update_tech_contact_id_error_component import (
        ApiV1DomainsDomainsUpdateTechContactIdErrorComponent,
    )
    from ..models.api_v1_domains_domains_update_tolerations_error_component import (
        ApiV1DomainsDomainsUpdateTolerationsErrorComponent,
    )
    from ..models.api_v1_domains_domains_update_transfer_lock_error_component import (
        ApiV1DomainsDomainsUpdateTransferLockErrorComponent,
    )
    from ..models.api_v1_domains_domains_update_use_platform_dns_error_component import (
        ApiV1DomainsDomainsUpdateUsePlatformDnsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1DomainsDomainsUpdateValidationError")


@_attrs_define
class ApiV1DomainsDomainsUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1DomainsDomainsUpdateAdminContactIdErrorComponent |
            ApiV1DomainsDomainsUpdateAnnotationsErrorComponent | ApiV1DomainsDomainsUpdateArchivedAtErrorComponent |
            ApiV1DomainsDomainsUpdateArchivedByErrorComponent | ApiV1DomainsDomainsUpdateArchivedErrorComponent |
            ApiV1DomainsDomainsUpdateArchivedReasonErrorComponent |
            ApiV1DomainsDomainsUpdateAuthCodeCredentialIdErrorComponent |
            ApiV1DomainsDomainsUpdateCreatedByComponentErrorComponent | ApiV1DomainsDomainsUpdateCreatedByUserErrorComponent
            | ApiV1DomainsDomainsUpdateCriticalityErrorComponent | ApiV1DomainsDomainsUpdateDebugModeErrorComponent |
            ApiV1DomainsDomainsUpdateDisplayNameErrorComponent | ApiV1DomainsDomainsUpdateDnsZoneIdErrorComponent |
            ApiV1DomainsDomainsUpdateExpiryDateErrorComponent | ApiV1DomainsDomainsUpdateKindErrorComponent |
            ApiV1DomainsDomainsUpdateLabelsErrorComponent |
            ApiV1DomainsDomainsUpdateLastReconciliationDurationSecondsErrorComponent |
            ApiV1DomainsDomainsUpdateManagedByContentTypeErrorComponent |
            ApiV1DomainsDomainsUpdateManagedByObjectIdErrorComponent | ApiV1DomainsDomainsUpdateModifiedByUserErrorComponent
            | ApiV1DomainsDomainsUpdateNameErrorComponent | ApiV1DomainsDomainsUpdateNameserversErrorComponent |
            ApiV1DomainsDomainsUpdateNonFieldErrorsErrorComponent | ApiV1DomainsDomainsUpdateOwnerContactIdErrorComponent |
            ApiV1DomainsDomainsUpdatePlatformDnsRecordCreatedErrorComponent |
            ApiV1DomainsDomainsUpdatePlatformServiceErrorComponent | ApiV1DomainsDomainsUpdateProviderErrorComponent |
            ApiV1DomainsDomainsUpdateProviderIdErrorComponent | ApiV1DomainsDomainsUpdateProviderReferenceErrorComponent |
            ApiV1DomainsDomainsUpdateProviderStatusErrorComponent |
            ApiV1DomainsDomainsUpdateReconciliationEnabledErrorComponent |
            ApiV1DomainsDomainsUpdateRegistrarDomainIdErrorComponent | ApiV1DomainsDomainsUpdateRegistrarIdErrorComponent |
            ApiV1DomainsDomainsUpdateRegistrarMetadataErrorComponent | ApiV1DomainsDomainsUpdateRenewalModeErrorComponent |
            ApiV1DomainsDomainsUpdateSlaAvailabilityErrorComponent | ApiV1DomainsDomainsUpdateSlaTargetErrorComponent |
            ApiV1DomainsDomainsUpdateSlaWindowDaysErrorComponent | ApiV1DomainsDomainsUpdateSloAvailabilityErrorComponent |
            ApiV1DomainsDomainsUpdateSloTargetErrorComponent | ApiV1DomainsDomainsUpdateSloWindowDaysErrorComponent |
            ApiV1DomainsDomainsUpdateTargetAvailabilityErrorComponent | ApiV1DomainsDomainsUpdateTechContactIdErrorComponent
            | ApiV1DomainsDomainsUpdateTolerationsErrorComponent | ApiV1DomainsDomainsUpdateTransferLockErrorComponent |
            ApiV1DomainsDomainsUpdateUsePlatformDnsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1DomainsDomainsUpdateAdminContactIdErrorComponent
        | ApiV1DomainsDomainsUpdateAnnotationsErrorComponent
        | ApiV1DomainsDomainsUpdateArchivedAtErrorComponent
        | ApiV1DomainsDomainsUpdateArchivedByErrorComponent
        | ApiV1DomainsDomainsUpdateArchivedErrorComponent
        | ApiV1DomainsDomainsUpdateArchivedReasonErrorComponent
        | ApiV1DomainsDomainsUpdateAuthCodeCredentialIdErrorComponent
        | ApiV1DomainsDomainsUpdateCreatedByComponentErrorComponent
        | ApiV1DomainsDomainsUpdateCreatedByUserErrorComponent
        | ApiV1DomainsDomainsUpdateCriticalityErrorComponent
        | ApiV1DomainsDomainsUpdateDebugModeErrorComponent
        | ApiV1DomainsDomainsUpdateDisplayNameErrorComponent
        | ApiV1DomainsDomainsUpdateDnsZoneIdErrorComponent
        | ApiV1DomainsDomainsUpdateExpiryDateErrorComponent
        | ApiV1DomainsDomainsUpdateKindErrorComponent
        | ApiV1DomainsDomainsUpdateLabelsErrorComponent
        | ApiV1DomainsDomainsUpdateLastReconciliationDurationSecondsErrorComponent
        | ApiV1DomainsDomainsUpdateManagedByContentTypeErrorComponent
        | ApiV1DomainsDomainsUpdateManagedByObjectIdErrorComponent
        | ApiV1DomainsDomainsUpdateModifiedByUserErrorComponent
        | ApiV1DomainsDomainsUpdateNameErrorComponent
        | ApiV1DomainsDomainsUpdateNameserversErrorComponent
        | ApiV1DomainsDomainsUpdateNonFieldErrorsErrorComponent
        | ApiV1DomainsDomainsUpdateOwnerContactIdErrorComponent
        | ApiV1DomainsDomainsUpdatePlatformDnsRecordCreatedErrorComponent
        | ApiV1DomainsDomainsUpdatePlatformServiceErrorComponent
        | ApiV1DomainsDomainsUpdateProviderErrorComponent
        | ApiV1DomainsDomainsUpdateProviderIdErrorComponent
        | ApiV1DomainsDomainsUpdateProviderReferenceErrorComponent
        | ApiV1DomainsDomainsUpdateProviderStatusErrorComponent
        | ApiV1DomainsDomainsUpdateReconciliationEnabledErrorComponent
        | ApiV1DomainsDomainsUpdateRegistrarDomainIdErrorComponent
        | ApiV1DomainsDomainsUpdateRegistrarIdErrorComponent
        | ApiV1DomainsDomainsUpdateRegistrarMetadataErrorComponent
        | ApiV1DomainsDomainsUpdateRenewalModeErrorComponent
        | ApiV1DomainsDomainsUpdateSlaAvailabilityErrorComponent
        | ApiV1DomainsDomainsUpdateSlaTargetErrorComponent
        | ApiV1DomainsDomainsUpdateSlaWindowDaysErrorComponent
        | ApiV1DomainsDomainsUpdateSloAvailabilityErrorComponent
        | ApiV1DomainsDomainsUpdateSloTargetErrorComponent
        | ApiV1DomainsDomainsUpdateSloWindowDaysErrorComponent
        | ApiV1DomainsDomainsUpdateTargetAvailabilityErrorComponent
        | ApiV1DomainsDomainsUpdateTechContactIdErrorComponent
        | ApiV1DomainsDomainsUpdateTolerationsErrorComponent
        | ApiV1DomainsDomainsUpdateTransferLockErrorComponent
        | ApiV1DomainsDomainsUpdateUsePlatformDnsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_domains_domains_update_admin_contact_id_error_component import (
            ApiV1DomainsDomainsUpdateAdminContactIdErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_annotations_error_component import (
            ApiV1DomainsDomainsUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_archived_at_error_component import (
            ApiV1DomainsDomainsUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_archived_by_error_component import (
            ApiV1DomainsDomainsUpdateArchivedByErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_archived_error_component import (
            ApiV1DomainsDomainsUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_archived_reason_error_component import (
            ApiV1DomainsDomainsUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_auth_code_credential_id_error_component import (
            ApiV1DomainsDomainsUpdateAuthCodeCredentialIdErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_created_by_component_error_component import (
            ApiV1DomainsDomainsUpdateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_criticality_error_component import (
            ApiV1DomainsDomainsUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_debug_mode_error_component import (
            ApiV1DomainsDomainsUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_display_name_error_component import (
            ApiV1DomainsDomainsUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_dns_zone_id_error_component import (
            ApiV1DomainsDomainsUpdateDnsZoneIdErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_expiry_date_error_component import (
            ApiV1DomainsDomainsUpdateExpiryDateErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_kind_error_component import (
            ApiV1DomainsDomainsUpdateKindErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_labels_error_component import (
            ApiV1DomainsDomainsUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_last_reconciliation_duration_seconds_error_component import (
            ApiV1DomainsDomainsUpdateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_managed_by_content_type_error_component import (
            ApiV1DomainsDomainsUpdateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_managed_by_object_id_error_component import (
            ApiV1DomainsDomainsUpdateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_modified_by_user_error_component import (
            ApiV1DomainsDomainsUpdateModifiedByUserErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_name_error_component import (
            ApiV1DomainsDomainsUpdateNameErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_nameservers_error_component import (
            ApiV1DomainsDomainsUpdateNameserversErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_non_field_errors_error_component import (
            ApiV1DomainsDomainsUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_owner_contact_id_error_component import (
            ApiV1DomainsDomainsUpdateOwnerContactIdErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_platform_dns_record_created_error_component import (
            ApiV1DomainsDomainsUpdatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_platform_service_error_component import (
            ApiV1DomainsDomainsUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_provider_error_component import (
            ApiV1DomainsDomainsUpdateProviderErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_provider_id_error_component import (
            ApiV1DomainsDomainsUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_provider_reference_error_component import (
            ApiV1DomainsDomainsUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_provider_status_error_component import (
            ApiV1DomainsDomainsUpdateProviderStatusErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_reconciliation_enabled_error_component import (
            ApiV1DomainsDomainsUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_registrar_domain_id_error_component import (
            ApiV1DomainsDomainsUpdateRegistrarDomainIdErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_registrar_id_error_component import (
            ApiV1DomainsDomainsUpdateRegistrarIdErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_registrar_metadata_error_component import (
            ApiV1DomainsDomainsUpdateRegistrarMetadataErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_renewal_mode_error_component import (
            ApiV1DomainsDomainsUpdateRenewalModeErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_sla_availability_error_component import (
            ApiV1DomainsDomainsUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_sla_target_error_component import (
            ApiV1DomainsDomainsUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_sla_window_days_error_component import (
            ApiV1DomainsDomainsUpdateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_slo_availability_error_component import (
            ApiV1DomainsDomainsUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_slo_target_error_component import (
            ApiV1DomainsDomainsUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_slo_window_days_error_component import (
            ApiV1DomainsDomainsUpdateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_target_availability_error_component import (
            ApiV1DomainsDomainsUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_tech_contact_id_error_component import (
            ApiV1DomainsDomainsUpdateTechContactIdErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_tolerations_error_component import (
            ApiV1DomainsDomainsUpdateTolerationsErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_transfer_lock_error_component import (
            ApiV1DomainsDomainsUpdateTransferLockErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_use_platform_dns_error_component import (
            ApiV1DomainsDomainsUpdateUsePlatformDnsErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1DomainsDomainsUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsUpdateRegistrarIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsUpdateDnsZoneIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsUpdateUsePlatformDnsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsUpdateOwnerContactIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsUpdateAdminContactIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsUpdateTechContactIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsUpdateAuthCodeCredentialIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsUpdateLastReconciliationDurationSecondsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsUpdateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsUpdateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsUpdateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsUpdateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsUpdatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsUpdateNameserversErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsUpdateRenewalModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsUpdateTransferLockErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsUpdateRegistrarDomainIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsUpdateProviderStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsUpdateExpiryDateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsUpdateRegistrarMetadataErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsUpdateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsUpdateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsUpdateModifiedByUserErrorComponent):
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
        from ..models.api_v1_domains_domains_update_admin_contact_id_error_component import (
            ApiV1DomainsDomainsUpdateAdminContactIdErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_annotations_error_component import (
            ApiV1DomainsDomainsUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_archived_at_error_component import (
            ApiV1DomainsDomainsUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_archived_by_error_component import (
            ApiV1DomainsDomainsUpdateArchivedByErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_archived_error_component import (
            ApiV1DomainsDomainsUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_archived_reason_error_component import (
            ApiV1DomainsDomainsUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_auth_code_credential_id_error_component import (
            ApiV1DomainsDomainsUpdateAuthCodeCredentialIdErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_created_by_component_error_component import (
            ApiV1DomainsDomainsUpdateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_created_by_user_error_component import (
            ApiV1DomainsDomainsUpdateCreatedByUserErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_criticality_error_component import (
            ApiV1DomainsDomainsUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_debug_mode_error_component import (
            ApiV1DomainsDomainsUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_display_name_error_component import (
            ApiV1DomainsDomainsUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_dns_zone_id_error_component import (
            ApiV1DomainsDomainsUpdateDnsZoneIdErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_expiry_date_error_component import (
            ApiV1DomainsDomainsUpdateExpiryDateErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_kind_error_component import (
            ApiV1DomainsDomainsUpdateKindErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_labels_error_component import (
            ApiV1DomainsDomainsUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_last_reconciliation_duration_seconds_error_component import (
            ApiV1DomainsDomainsUpdateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_managed_by_content_type_error_component import (
            ApiV1DomainsDomainsUpdateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_managed_by_object_id_error_component import (
            ApiV1DomainsDomainsUpdateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_modified_by_user_error_component import (
            ApiV1DomainsDomainsUpdateModifiedByUserErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_name_error_component import (
            ApiV1DomainsDomainsUpdateNameErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_nameservers_error_component import (
            ApiV1DomainsDomainsUpdateNameserversErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_non_field_errors_error_component import (
            ApiV1DomainsDomainsUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_owner_contact_id_error_component import (
            ApiV1DomainsDomainsUpdateOwnerContactIdErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_platform_dns_record_created_error_component import (
            ApiV1DomainsDomainsUpdatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_platform_service_error_component import (
            ApiV1DomainsDomainsUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_provider_error_component import (
            ApiV1DomainsDomainsUpdateProviderErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_provider_id_error_component import (
            ApiV1DomainsDomainsUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_provider_reference_error_component import (
            ApiV1DomainsDomainsUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_provider_status_error_component import (
            ApiV1DomainsDomainsUpdateProviderStatusErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_reconciliation_enabled_error_component import (
            ApiV1DomainsDomainsUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_registrar_domain_id_error_component import (
            ApiV1DomainsDomainsUpdateRegistrarDomainIdErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_registrar_id_error_component import (
            ApiV1DomainsDomainsUpdateRegistrarIdErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_registrar_metadata_error_component import (
            ApiV1DomainsDomainsUpdateRegistrarMetadataErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_renewal_mode_error_component import (
            ApiV1DomainsDomainsUpdateRenewalModeErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_sla_availability_error_component import (
            ApiV1DomainsDomainsUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_sla_target_error_component import (
            ApiV1DomainsDomainsUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_sla_window_days_error_component import (
            ApiV1DomainsDomainsUpdateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_slo_availability_error_component import (
            ApiV1DomainsDomainsUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_slo_target_error_component import (
            ApiV1DomainsDomainsUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_slo_window_days_error_component import (
            ApiV1DomainsDomainsUpdateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_target_availability_error_component import (
            ApiV1DomainsDomainsUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_tech_contact_id_error_component import (
            ApiV1DomainsDomainsUpdateTechContactIdErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_tolerations_error_component import (
            ApiV1DomainsDomainsUpdateTolerationsErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_transfer_lock_error_component import (
            ApiV1DomainsDomainsUpdateTransferLockErrorComponent,
        )
        from ..models.api_v1_domains_domains_update_use_platform_dns_error_component import (
            ApiV1DomainsDomainsUpdateUsePlatformDnsErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1DomainsDomainsUpdateAdminContactIdErrorComponent
                | ApiV1DomainsDomainsUpdateAnnotationsErrorComponent
                | ApiV1DomainsDomainsUpdateArchivedAtErrorComponent
                | ApiV1DomainsDomainsUpdateArchivedByErrorComponent
                | ApiV1DomainsDomainsUpdateArchivedErrorComponent
                | ApiV1DomainsDomainsUpdateArchivedReasonErrorComponent
                | ApiV1DomainsDomainsUpdateAuthCodeCredentialIdErrorComponent
                | ApiV1DomainsDomainsUpdateCreatedByComponentErrorComponent
                | ApiV1DomainsDomainsUpdateCreatedByUserErrorComponent
                | ApiV1DomainsDomainsUpdateCriticalityErrorComponent
                | ApiV1DomainsDomainsUpdateDebugModeErrorComponent
                | ApiV1DomainsDomainsUpdateDisplayNameErrorComponent
                | ApiV1DomainsDomainsUpdateDnsZoneIdErrorComponent
                | ApiV1DomainsDomainsUpdateExpiryDateErrorComponent
                | ApiV1DomainsDomainsUpdateKindErrorComponent
                | ApiV1DomainsDomainsUpdateLabelsErrorComponent
                | ApiV1DomainsDomainsUpdateLastReconciliationDurationSecondsErrorComponent
                | ApiV1DomainsDomainsUpdateManagedByContentTypeErrorComponent
                | ApiV1DomainsDomainsUpdateManagedByObjectIdErrorComponent
                | ApiV1DomainsDomainsUpdateModifiedByUserErrorComponent
                | ApiV1DomainsDomainsUpdateNameErrorComponent
                | ApiV1DomainsDomainsUpdateNameserversErrorComponent
                | ApiV1DomainsDomainsUpdateNonFieldErrorsErrorComponent
                | ApiV1DomainsDomainsUpdateOwnerContactIdErrorComponent
                | ApiV1DomainsDomainsUpdatePlatformDnsRecordCreatedErrorComponent
                | ApiV1DomainsDomainsUpdatePlatformServiceErrorComponent
                | ApiV1DomainsDomainsUpdateProviderErrorComponent
                | ApiV1DomainsDomainsUpdateProviderIdErrorComponent
                | ApiV1DomainsDomainsUpdateProviderReferenceErrorComponent
                | ApiV1DomainsDomainsUpdateProviderStatusErrorComponent
                | ApiV1DomainsDomainsUpdateReconciliationEnabledErrorComponent
                | ApiV1DomainsDomainsUpdateRegistrarDomainIdErrorComponent
                | ApiV1DomainsDomainsUpdateRegistrarIdErrorComponent
                | ApiV1DomainsDomainsUpdateRegistrarMetadataErrorComponent
                | ApiV1DomainsDomainsUpdateRenewalModeErrorComponent
                | ApiV1DomainsDomainsUpdateSlaAvailabilityErrorComponent
                | ApiV1DomainsDomainsUpdateSlaTargetErrorComponent
                | ApiV1DomainsDomainsUpdateSlaWindowDaysErrorComponent
                | ApiV1DomainsDomainsUpdateSloAvailabilityErrorComponent
                | ApiV1DomainsDomainsUpdateSloTargetErrorComponent
                | ApiV1DomainsDomainsUpdateSloWindowDaysErrorComponent
                | ApiV1DomainsDomainsUpdateTargetAvailabilityErrorComponent
                | ApiV1DomainsDomainsUpdateTechContactIdErrorComponent
                | ApiV1DomainsDomainsUpdateTolerationsErrorComponent
                | ApiV1DomainsDomainsUpdateTransferLockErrorComponent
                | ApiV1DomainsDomainsUpdateUsePlatformDnsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_update_error_type_0 = (
                        ApiV1DomainsDomainsUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_update_error_type_1 = (
                        ApiV1DomainsDomainsUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_update_error_type_2 = (
                        ApiV1DomainsDomainsUpdateRegistrarIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_update_error_type_3 = (
                        ApiV1DomainsDomainsUpdateDnsZoneIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_update_error_type_4 = (
                        ApiV1DomainsDomainsUpdateUsePlatformDnsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_update_error_type_5 = (
                        ApiV1DomainsDomainsUpdateOwnerContactIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_update_error_type_6 = (
                        ApiV1DomainsDomainsUpdateAdminContactIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_update_error_type_7 = (
                        ApiV1DomainsDomainsUpdateTechContactIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_update_error_type_8 = (
                        ApiV1DomainsDomainsUpdateAuthCodeCredentialIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_update_error_type_9 = (
                        ApiV1DomainsDomainsUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_update_error_type_10 = (
                        ApiV1DomainsDomainsUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_update_error_type_11 = (
                        ApiV1DomainsDomainsUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_update_error_type_12 = (
                        ApiV1DomainsDomainsUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_update_error_type_13 = (
                        ApiV1DomainsDomainsUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_update_error_type_14 = (
                        ApiV1DomainsDomainsUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_update_error_type_15 = (
                        ApiV1DomainsDomainsUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_update_error_type_16 = (
                        ApiV1DomainsDomainsUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_update_error_type_17 = (
                        ApiV1DomainsDomainsUpdateLastReconciliationDurationSecondsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_update_error_type_18 = (
                        ApiV1DomainsDomainsUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_update_error_type_19 = (
                        ApiV1DomainsDomainsUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_update_error_type_20 = (
                        ApiV1DomainsDomainsUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_update_error_type_21 = (
                        ApiV1DomainsDomainsUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_update_error_type_22 = (
                        ApiV1DomainsDomainsUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_update_error_type_23 = (
                        ApiV1DomainsDomainsUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_update_error_type_24 = (
                        ApiV1DomainsDomainsUpdateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_update_error_type_25 = (
                        ApiV1DomainsDomainsUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_update_error_type_26 = (
                        ApiV1DomainsDomainsUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_update_error_type_27 = (
                        ApiV1DomainsDomainsUpdateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_update_error_type_28 = (
                        ApiV1DomainsDomainsUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_update_error_type_29 = (
                        ApiV1DomainsDomainsUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_update_error_type_30 = (
                        ApiV1DomainsDomainsUpdateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_update_error_type_31 = (
                        ApiV1DomainsDomainsUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_update_error_type_32 = (
                        ApiV1DomainsDomainsUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_update_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_update_error_type_33 = (
                        ApiV1DomainsDomainsUpdateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_update_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_update_error_type_34 = (
                        ApiV1DomainsDomainsUpdatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_update_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_update_error_type_35 = (
                        ApiV1DomainsDomainsUpdateNameserversErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_update_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_update_error_type_36 = (
                        ApiV1DomainsDomainsUpdateRenewalModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_update_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_update_error_type_37 = (
                        ApiV1DomainsDomainsUpdateTransferLockErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_update_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_update_error_type_38 = (
                        ApiV1DomainsDomainsUpdateRegistrarDomainIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_update_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_update_error_type_39 = (
                        ApiV1DomainsDomainsUpdateProviderStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_update_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_update_error_type_40 = (
                        ApiV1DomainsDomainsUpdateExpiryDateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_update_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_update_error_type_41 = (
                        ApiV1DomainsDomainsUpdateRegistrarMetadataErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_update_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_update_error_type_42 = (
                        ApiV1DomainsDomainsUpdateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_update_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_update_error_type_43 = (
                        ApiV1DomainsDomainsUpdateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_update_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_update_error_type_44 = (
                        ApiV1DomainsDomainsUpdateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_update_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_domains_domains_update_error_type_45 = (
                    ApiV1DomainsDomainsUpdateCreatedByUserErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_domains_domains_update_error_type_45

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_domains_domains_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_domains_domains_update_validation_error.additional_properties = d
        return api_v1_domains_domains_update_validation_error

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
