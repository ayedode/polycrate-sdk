from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_domains_dnsrecords_partial_update_annotations_error_component import (
        ApiV1DomainsDnsrecordsPartialUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_partial_update_archived_at_error_component import (
        ApiV1DomainsDnsrecordsPartialUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_partial_update_archived_by_error_component import (
        ApiV1DomainsDnsrecordsPartialUpdateArchivedByErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_partial_update_archived_error_component import (
        ApiV1DomainsDnsrecordsPartialUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_partial_update_archived_reason_error_component import (
        ApiV1DomainsDnsrecordsPartialUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_partial_update_content_error_component import (
        ApiV1DomainsDnsrecordsPartialUpdateContentErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_partial_update_created_by_component_error_component import (
        ApiV1DomainsDnsrecordsPartialUpdateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_partial_update_created_by_user_error_component import (
        ApiV1DomainsDnsrecordsPartialUpdateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_partial_update_criticality_error_component import (
        ApiV1DomainsDnsrecordsPartialUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_partial_update_debug_mode_error_component import (
        ApiV1DomainsDnsrecordsPartialUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_partial_update_display_name_error_component import (
        ApiV1DomainsDnsrecordsPartialUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_partial_update_dns_zone_id_error_component import (
        ApiV1DomainsDnsrecordsPartialUpdateDnsZoneIdErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_partial_update_kind_error_component import (
        ApiV1DomainsDnsrecordsPartialUpdateKindErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_partial_update_labels_error_component import (
        ApiV1DomainsDnsrecordsPartialUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_partial_update_last_reconciliation_duration_seconds_error_component import (
        ApiV1DomainsDnsrecordsPartialUpdateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_partial_update_managed_by_content_type_error_component import (
        ApiV1DomainsDnsrecordsPartialUpdateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_partial_update_managed_by_object_id_error_component import (
        ApiV1DomainsDnsrecordsPartialUpdateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_partial_update_modified_by_user_error_component import (
        ApiV1DomainsDnsrecordsPartialUpdateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_partial_update_name_error_component import (
        ApiV1DomainsDnsrecordsPartialUpdateNameErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_partial_update_non_field_errors_error_component import (
        ApiV1DomainsDnsrecordsPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_partial_update_platform_dns_record_created_error_component import (
        ApiV1DomainsDnsrecordsPartialUpdatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_partial_update_platform_service_error_component import (
        ApiV1DomainsDnsrecordsPartialUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_partial_update_priority_error_component import (
        ApiV1DomainsDnsrecordsPartialUpdatePriorityErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_partial_update_provider_error_component import (
        ApiV1DomainsDnsrecordsPartialUpdateProviderErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_partial_update_provider_id_error_component import (
        ApiV1DomainsDnsrecordsPartialUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_partial_update_provider_reference_error_component import (
        ApiV1DomainsDnsrecordsPartialUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_partial_update_reconciliation_enabled_error_component import (
        ApiV1DomainsDnsrecordsPartialUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_partial_update_sla_availability_error_component import (
        ApiV1DomainsDnsrecordsPartialUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_partial_update_sla_target_error_component import (
        ApiV1DomainsDnsrecordsPartialUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_partial_update_sla_window_days_error_component import (
        ApiV1DomainsDnsrecordsPartialUpdateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_partial_update_slo_availability_error_component import (
        ApiV1DomainsDnsrecordsPartialUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_partial_update_slo_target_error_component import (
        ApiV1DomainsDnsrecordsPartialUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_partial_update_slo_window_days_error_component import (
        ApiV1DomainsDnsrecordsPartialUpdateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_partial_update_target_availability_error_component import (
        ApiV1DomainsDnsrecordsPartialUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_partial_update_tolerations_error_component import (
        ApiV1DomainsDnsrecordsPartialUpdateTolerationsErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_partial_update_ttl_error_component import (
        ApiV1DomainsDnsrecordsPartialUpdateTtlErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_partial_update_type_error_component import (
        ApiV1DomainsDnsrecordsPartialUpdateTypeErrorComponent,
    )


T = TypeVar("T", bound="ApiV1DomainsDnsrecordsPartialUpdateValidationError")


@_attrs_define
class ApiV1DomainsDnsrecordsPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1DomainsDnsrecordsPartialUpdateAnnotationsErrorComponent |
            ApiV1DomainsDnsrecordsPartialUpdateArchivedAtErrorComponent |
            ApiV1DomainsDnsrecordsPartialUpdateArchivedByErrorComponent |
            ApiV1DomainsDnsrecordsPartialUpdateArchivedErrorComponent |
            ApiV1DomainsDnsrecordsPartialUpdateArchivedReasonErrorComponent |
            ApiV1DomainsDnsrecordsPartialUpdateContentErrorComponent |
            ApiV1DomainsDnsrecordsPartialUpdateCreatedByComponentErrorComponent |
            ApiV1DomainsDnsrecordsPartialUpdateCreatedByUserErrorComponent |
            ApiV1DomainsDnsrecordsPartialUpdateCriticalityErrorComponent |
            ApiV1DomainsDnsrecordsPartialUpdateDebugModeErrorComponent |
            ApiV1DomainsDnsrecordsPartialUpdateDisplayNameErrorComponent |
            ApiV1DomainsDnsrecordsPartialUpdateDnsZoneIdErrorComponent |
            ApiV1DomainsDnsrecordsPartialUpdateKindErrorComponent | ApiV1DomainsDnsrecordsPartialUpdateLabelsErrorComponent
            | ApiV1DomainsDnsrecordsPartialUpdateLastReconciliationDurationSecondsErrorComponent |
            ApiV1DomainsDnsrecordsPartialUpdateManagedByContentTypeErrorComponent |
            ApiV1DomainsDnsrecordsPartialUpdateManagedByObjectIdErrorComponent |
            ApiV1DomainsDnsrecordsPartialUpdateModifiedByUserErrorComponent |
            ApiV1DomainsDnsrecordsPartialUpdateNameErrorComponent |
            ApiV1DomainsDnsrecordsPartialUpdateNonFieldErrorsErrorComponent |
            ApiV1DomainsDnsrecordsPartialUpdatePlatformDnsRecordCreatedErrorComponent |
            ApiV1DomainsDnsrecordsPartialUpdatePlatformServiceErrorComponent |
            ApiV1DomainsDnsrecordsPartialUpdatePriorityErrorComponent |
            ApiV1DomainsDnsrecordsPartialUpdateProviderErrorComponent |
            ApiV1DomainsDnsrecordsPartialUpdateProviderIdErrorComponent |
            ApiV1DomainsDnsrecordsPartialUpdateProviderReferenceErrorComponent |
            ApiV1DomainsDnsrecordsPartialUpdateReconciliationEnabledErrorComponent |
            ApiV1DomainsDnsrecordsPartialUpdateSlaAvailabilityErrorComponent |
            ApiV1DomainsDnsrecordsPartialUpdateSlaTargetErrorComponent |
            ApiV1DomainsDnsrecordsPartialUpdateSlaWindowDaysErrorComponent |
            ApiV1DomainsDnsrecordsPartialUpdateSloAvailabilityErrorComponent |
            ApiV1DomainsDnsrecordsPartialUpdateSloTargetErrorComponent |
            ApiV1DomainsDnsrecordsPartialUpdateSloWindowDaysErrorComponent |
            ApiV1DomainsDnsrecordsPartialUpdateTargetAvailabilityErrorComponent |
            ApiV1DomainsDnsrecordsPartialUpdateTolerationsErrorComponent |
            ApiV1DomainsDnsrecordsPartialUpdateTtlErrorComponent | ApiV1DomainsDnsrecordsPartialUpdateTypeErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1DomainsDnsrecordsPartialUpdateAnnotationsErrorComponent
        | ApiV1DomainsDnsrecordsPartialUpdateArchivedAtErrorComponent
        | ApiV1DomainsDnsrecordsPartialUpdateArchivedByErrorComponent
        | ApiV1DomainsDnsrecordsPartialUpdateArchivedErrorComponent
        | ApiV1DomainsDnsrecordsPartialUpdateArchivedReasonErrorComponent
        | ApiV1DomainsDnsrecordsPartialUpdateContentErrorComponent
        | ApiV1DomainsDnsrecordsPartialUpdateCreatedByComponentErrorComponent
        | ApiV1DomainsDnsrecordsPartialUpdateCreatedByUserErrorComponent
        | ApiV1DomainsDnsrecordsPartialUpdateCriticalityErrorComponent
        | ApiV1DomainsDnsrecordsPartialUpdateDebugModeErrorComponent
        | ApiV1DomainsDnsrecordsPartialUpdateDisplayNameErrorComponent
        | ApiV1DomainsDnsrecordsPartialUpdateDnsZoneIdErrorComponent
        | ApiV1DomainsDnsrecordsPartialUpdateKindErrorComponent
        | ApiV1DomainsDnsrecordsPartialUpdateLabelsErrorComponent
        | ApiV1DomainsDnsrecordsPartialUpdateLastReconciliationDurationSecondsErrorComponent
        | ApiV1DomainsDnsrecordsPartialUpdateManagedByContentTypeErrorComponent
        | ApiV1DomainsDnsrecordsPartialUpdateManagedByObjectIdErrorComponent
        | ApiV1DomainsDnsrecordsPartialUpdateModifiedByUserErrorComponent
        | ApiV1DomainsDnsrecordsPartialUpdateNameErrorComponent
        | ApiV1DomainsDnsrecordsPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1DomainsDnsrecordsPartialUpdatePlatformDnsRecordCreatedErrorComponent
        | ApiV1DomainsDnsrecordsPartialUpdatePlatformServiceErrorComponent
        | ApiV1DomainsDnsrecordsPartialUpdatePriorityErrorComponent
        | ApiV1DomainsDnsrecordsPartialUpdateProviderErrorComponent
        | ApiV1DomainsDnsrecordsPartialUpdateProviderIdErrorComponent
        | ApiV1DomainsDnsrecordsPartialUpdateProviderReferenceErrorComponent
        | ApiV1DomainsDnsrecordsPartialUpdateReconciliationEnabledErrorComponent
        | ApiV1DomainsDnsrecordsPartialUpdateSlaAvailabilityErrorComponent
        | ApiV1DomainsDnsrecordsPartialUpdateSlaTargetErrorComponent
        | ApiV1DomainsDnsrecordsPartialUpdateSlaWindowDaysErrorComponent
        | ApiV1DomainsDnsrecordsPartialUpdateSloAvailabilityErrorComponent
        | ApiV1DomainsDnsrecordsPartialUpdateSloTargetErrorComponent
        | ApiV1DomainsDnsrecordsPartialUpdateSloWindowDaysErrorComponent
        | ApiV1DomainsDnsrecordsPartialUpdateTargetAvailabilityErrorComponent
        | ApiV1DomainsDnsrecordsPartialUpdateTolerationsErrorComponent
        | ApiV1DomainsDnsrecordsPartialUpdateTtlErrorComponent
        | ApiV1DomainsDnsrecordsPartialUpdateTypeErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_domains_dnsrecords_partial_update_annotations_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_archived_at_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_archived_by_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdateArchivedByErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_archived_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_archived_reason_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_content_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdateContentErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_created_by_component_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_criticality_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_debug_mode_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_display_name_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_dns_zone_id_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdateDnsZoneIdErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_kind_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdateKindErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_labels_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_last_reconciliation_duration_seconds_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_managed_by_content_type_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_managed_by_object_id_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_modified_by_user_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdateModifiedByUserErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_name_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_non_field_errors_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_platform_dns_record_created_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_platform_service_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_priority_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdatePriorityErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_provider_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_provider_id_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_provider_reference_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_reconciliation_enabled_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_sla_availability_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_sla_target_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_sla_window_days_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_slo_availability_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_slo_target_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_slo_window_days_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_target_availability_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_tolerations_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdateTolerationsErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_ttl_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdateTtlErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_type_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdateTypeErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1DomainsDnsrecordsPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsPartialUpdateDnsZoneIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsPartialUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsPartialUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsPartialUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsPartialUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsPartialUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsPartialUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsPartialUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsPartialUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1DomainsDnsrecordsPartialUpdateLastReconciliationDurationSecondsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsPartialUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsPartialUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsPartialUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsPartialUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsPartialUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsPartialUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsPartialUpdateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsPartialUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsPartialUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsPartialUpdateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsPartialUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsPartialUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsPartialUpdateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsPartialUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsPartialUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsPartialUpdateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1DomainsDnsrecordsPartialUpdatePlatformDnsRecordCreatedErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsPartialUpdateTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsPartialUpdateContentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsPartialUpdateTtlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsPartialUpdatePriorityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsPartialUpdateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsPartialUpdateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsPartialUpdateModifiedByUserErrorComponent):
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
        from ..models.api_v1_domains_dnsrecords_partial_update_annotations_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_archived_at_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_archived_by_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdateArchivedByErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_archived_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_archived_reason_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_content_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdateContentErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_created_by_component_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_created_by_user_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdateCreatedByUserErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_criticality_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_debug_mode_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_display_name_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_dns_zone_id_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdateDnsZoneIdErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_kind_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdateKindErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_labels_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_last_reconciliation_duration_seconds_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_managed_by_content_type_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_managed_by_object_id_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_modified_by_user_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdateModifiedByUserErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_name_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_non_field_errors_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_platform_dns_record_created_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_platform_service_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_priority_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdatePriorityErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_provider_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_provider_id_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_provider_reference_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_reconciliation_enabled_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_sla_availability_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_sla_target_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_sla_window_days_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_slo_availability_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_slo_target_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_slo_window_days_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_target_availability_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_tolerations_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdateTolerationsErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_ttl_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdateTtlErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_partial_update_type_error_component import (
            ApiV1DomainsDnsrecordsPartialUpdateTypeErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1DomainsDnsrecordsPartialUpdateAnnotationsErrorComponent
                | ApiV1DomainsDnsrecordsPartialUpdateArchivedAtErrorComponent
                | ApiV1DomainsDnsrecordsPartialUpdateArchivedByErrorComponent
                | ApiV1DomainsDnsrecordsPartialUpdateArchivedErrorComponent
                | ApiV1DomainsDnsrecordsPartialUpdateArchivedReasonErrorComponent
                | ApiV1DomainsDnsrecordsPartialUpdateContentErrorComponent
                | ApiV1DomainsDnsrecordsPartialUpdateCreatedByComponentErrorComponent
                | ApiV1DomainsDnsrecordsPartialUpdateCreatedByUserErrorComponent
                | ApiV1DomainsDnsrecordsPartialUpdateCriticalityErrorComponent
                | ApiV1DomainsDnsrecordsPartialUpdateDebugModeErrorComponent
                | ApiV1DomainsDnsrecordsPartialUpdateDisplayNameErrorComponent
                | ApiV1DomainsDnsrecordsPartialUpdateDnsZoneIdErrorComponent
                | ApiV1DomainsDnsrecordsPartialUpdateKindErrorComponent
                | ApiV1DomainsDnsrecordsPartialUpdateLabelsErrorComponent
                | ApiV1DomainsDnsrecordsPartialUpdateLastReconciliationDurationSecondsErrorComponent
                | ApiV1DomainsDnsrecordsPartialUpdateManagedByContentTypeErrorComponent
                | ApiV1DomainsDnsrecordsPartialUpdateManagedByObjectIdErrorComponent
                | ApiV1DomainsDnsrecordsPartialUpdateModifiedByUserErrorComponent
                | ApiV1DomainsDnsrecordsPartialUpdateNameErrorComponent
                | ApiV1DomainsDnsrecordsPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1DomainsDnsrecordsPartialUpdatePlatformDnsRecordCreatedErrorComponent
                | ApiV1DomainsDnsrecordsPartialUpdatePlatformServiceErrorComponent
                | ApiV1DomainsDnsrecordsPartialUpdatePriorityErrorComponent
                | ApiV1DomainsDnsrecordsPartialUpdateProviderErrorComponent
                | ApiV1DomainsDnsrecordsPartialUpdateProviderIdErrorComponent
                | ApiV1DomainsDnsrecordsPartialUpdateProviderReferenceErrorComponent
                | ApiV1DomainsDnsrecordsPartialUpdateReconciliationEnabledErrorComponent
                | ApiV1DomainsDnsrecordsPartialUpdateSlaAvailabilityErrorComponent
                | ApiV1DomainsDnsrecordsPartialUpdateSlaTargetErrorComponent
                | ApiV1DomainsDnsrecordsPartialUpdateSlaWindowDaysErrorComponent
                | ApiV1DomainsDnsrecordsPartialUpdateSloAvailabilityErrorComponent
                | ApiV1DomainsDnsrecordsPartialUpdateSloTargetErrorComponent
                | ApiV1DomainsDnsrecordsPartialUpdateSloWindowDaysErrorComponent
                | ApiV1DomainsDnsrecordsPartialUpdateTargetAvailabilityErrorComponent
                | ApiV1DomainsDnsrecordsPartialUpdateTolerationsErrorComponent
                | ApiV1DomainsDnsrecordsPartialUpdateTtlErrorComponent
                | ApiV1DomainsDnsrecordsPartialUpdateTypeErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_0 = (
                        ApiV1DomainsDnsrecordsPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_1 = (
                        ApiV1DomainsDnsrecordsPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_2 = (
                        ApiV1DomainsDnsrecordsPartialUpdateDnsZoneIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_3 = (
                        ApiV1DomainsDnsrecordsPartialUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_4 = (
                        ApiV1DomainsDnsrecordsPartialUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_5 = (
                        ApiV1DomainsDnsrecordsPartialUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_6 = (
                        ApiV1DomainsDnsrecordsPartialUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_7 = (
                        ApiV1DomainsDnsrecordsPartialUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_8 = (
                        ApiV1DomainsDnsrecordsPartialUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_9 = (
                        ApiV1DomainsDnsrecordsPartialUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_10 = (
                        ApiV1DomainsDnsrecordsPartialUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_11 = (
                        ApiV1DomainsDnsrecordsPartialUpdateLastReconciliationDurationSecondsErrorComponent.from_dict(
                            data
                        )
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_12 = (
                        ApiV1DomainsDnsrecordsPartialUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_13 = (
                        ApiV1DomainsDnsrecordsPartialUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_14 = (
                        ApiV1DomainsDnsrecordsPartialUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_15 = (
                        ApiV1DomainsDnsrecordsPartialUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_16 = (
                        ApiV1DomainsDnsrecordsPartialUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_17 = (
                        ApiV1DomainsDnsrecordsPartialUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_18 = (
                        ApiV1DomainsDnsrecordsPartialUpdateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_19 = (
                        ApiV1DomainsDnsrecordsPartialUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_20 = (
                        ApiV1DomainsDnsrecordsPartialUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_21 = (
                        ApiV1DomainsDnsrecordsPartialUpdateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_22 = (
                        ApiV1DomainsDnsrecordsPartialUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_23 = (
                        ApiV1DomainsDnsrecordsPartialUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_24 = (
                        ApiV1DomainsDnsrecordsPartialUpdateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_25 = (
                        ApiV1DomainsDnsrecordsPartialUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_26 = (
                        ApiV1DomainsDnsrecordsPartialUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_27 = (
                        ApiV1DomainsDnsrecordsPartialUpdateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_28 = (
                        ApiV1DomainsDnsrecordsPartialUpdatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_29 = (
                        ApiV1DomainsDnsrecordsPartialUpdateTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_30 = (
                        ApiV1DomainsDnsrecordsPartialUpdateContentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_31 = (
                        ApiV1DomainsDnsrecordsPartialUpdateTtlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_32 = (
                        ApiV1DomainsDnsrecordsPartialUpdatePriorityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_33 = (
                        ApiV1DomainsDnsrecordsPartialUpdateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_34 = (
                        ApiV1DomainsDnsrecordsPartialUpdateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_35 = (
                        ApiV1DomainsDnsrecordsPartialUpdateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_36 = (
                    ApiV1DomainsDnsrecordsPartialUpdateCreatedByUserErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_domains_dnsrecords_partial_update_error_type_36

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_domains_dnsrecords_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_domains_dnsrecords_partial_update_validation_error.additional_properties = d
        return api_v1_domains_dnsrecords_partial_update_validation_error

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
