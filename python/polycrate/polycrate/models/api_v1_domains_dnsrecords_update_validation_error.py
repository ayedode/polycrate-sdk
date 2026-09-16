from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_domains_dnsrecords_update_annotations_error_component import (
        ApiV1DomainsDnsrecordsUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_update_archived_at_error_component import (
        ApiV1DomainsDnsrecordsUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_update_archived_by_error_component import (
        ApiV1DomainsDnsrecordsUpdateArchivedByErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_update_archived_error_component import (
        ApiV1DomainsDnsrecordsUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_update_archived_reason_error_component import (
        ApiV1DomainsDnsrecordsUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_update_content_error_component import (
        ApiV1DomainsDnsrecordsUpdateContentErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_update_created_by_component_error_component import (
        ApiV1DomainsDnsrecordsUpdateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_update_created_by_user_error_component import (
        ApiV1DomainsDnsrecordsUpdateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_update_criticality_error_component import (
        ApiV1DomainsDnsrecordsUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_update_debug_mode_error_component import (
        ApiV1DomainsDnsrecordsUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_update_display_name_error_component import (
        ApiV1DomainsDnsrecordsUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_update_dns_zone_id_error_component import (
        ApiV1DomainsDnsrecordsUpdateDnsZoneIdErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_update_kind_error_component import (
        ApiV1DomainsDnsrecordsUpdateKindErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_update_labels_error_component import (
        ApiV1DomainsDnsrecordsUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_update_last_reconciliation_duration_seconds_error_component import (
        ApiV1DomainsDnsrecordsUpdateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_update_managed_by_content_type_error_component import (
        ApiV1DomainsDnsrecordsUpdateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_update_managed_by_object_id_error_component import (
        ApiV1DomainsDnsrecordsUpdateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_update_modified_by_user_error_component import (
        ApiV1DomainsDnsrecordsUpdateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_update_name_error_component import (
        ApiV1DomainsDnsrecordsUpdateNameErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_update_non_field_errors_error_component import (
        ApiV1DomainsDnsrecordsUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_update_platform_dns_record_created_error_component import (
        ApiV1DomainsDnsrecordsUpdatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_update_platform_service_error_component import (
        ApiV1DomainsDnsrecordsUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_update_priority_error_component import (
        ApiV1DomainsDnsrecordsUpdatePriorityErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_update_provider_error_component import (
        ApiV1DomainsDnsrecordsUpdateProviderErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_update_provider_id_error_component import (
        ApiV1DomainsDnsrecordsUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_update_provider_reference_error_component import (
        ApiV1DomainsDnsrecordsUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_update_reconciliation_enabled_error_component import (
        ApiV1DomainsDnsrecordsUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_update_sla_availability_error_component import (
        ApiV1DomainsDnsrecordsUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_update_sla_target_error_component import (
        ApiV1DomainsDnsrecordsUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_update_sla_window_days_error_component import (
        ApiV1DomainsDnsrecordsUpdateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_update_slo_availability_error_component import (
        ApiV1DomainsDnsrecordsUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_update_slo_target_error_component import (
        ApiV1DomainsDnsrecordsUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_update_slo_window_days_error_component import (
        ApiV1DomainsDnsrecordsUpdateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_update_target_availability_error_component import (
        ApiV1DomainsDnsrecordsUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_update_tolerations_error_component import (
        ApiV1DomainsDnsrecordsUpdateTolerationsErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_update_ttl_error_component import (
        ApiV1DomainsDnsrecordsUpdateTtlErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_update_type_error_component import (
        ApiV1DomainsDnsrecordsUpdateTypeErrorComponent,
    )


T = TypeVar("T", bound="ApiV1DomainsDnsrecordsUpdateValidationError")


@_attrs_define
class ApiV1DomainsDnsrecordsUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1DomainsDnsrecordsUpdateAnnotationsErrorComponent |
            ApiV1DomainsDnsrecordsUpdateArchivedAtErrorComponent | ApiV1DomainsDnsrecordsUpdateArchivedByErrorComponent |
            ApiV1DomainsDnsrecordsUpdateArchivedErrorComponent | ApiV1DomainsDnsrecordsUpdateArchivedReasonErrorComponent |
            ApiV1DomainsDnsrecordsUpdateContentErrorComponent | ApiV1DomainsDnsrecordsUpdateCreatedByComponentErrorComponent
            | ApiV1DomainsDnsrecordsUpdateCreatedByUserErrorComponent |
            ApiV1DomainsDnsrecordsUpdateCriticalityErrorComponent | ApiV1DomainsDnsrecordsUpdateDebugModeErrorComponent |
            ApiV1DomainsDnsrecordsUpdateDisplayNameErrorComponent | ApiV1DomainsDnsrecordsUpdateDnsZoneIdErrorComponent |
            ApiV1DomainsDnsrecordsUpdateKindErrorComponent | ApiV1DomainsDnsrecordsUpdateLabelsErrorComponent |
            ApiV1DomainsDnsrecordsUpdateLastReconciliationDurationSecondsErrorComponent |
            ApiV1DomainsDnsrecordsUpdateManagedByContentTypeErrorComponent |
            ApiV1DomainsDnsrecordsUpdateManagedByObjectIdErrorComponent |
            ApiV1DomainsDnsrecordsUpdateModifiedByUserErrorComponent | ApiV1DomainsDnsrecordsUpdateNameErrorComponent |
            ApiV1DomainsDnsrecordsUpdateNonFieldErrorsErrorComponent |
            ApiV1DomainsDnsrecordsUpdatePlatformDnsRecordCreatedErrorComponent |
            ApiV1DomainsDnsrecordsUpdatePlatformServiceErrorComponent | ApiV1DomainsDnsrecordsUpdatePriorityErrorComponent |
            ApiV1DomainsDnsrecordsUpdateProviderErrorComponent | ApiV1DomainsDnsrecordsUpdateProviderIdErrorComponent |
            ApiV1DomainsDnsrecordsUpdateProviderReferenceErrorComponent |
            ApiV1DomainsDnsrecordsUpdateReconciliationEnabledErrorComponent |
            ApiV1DomainsDnsrecordsUpdateSlaAvailabilityErrorComponent | ApiV1DomainsDnsrecordsUpdateSlaTargetErrorComponent
            | ApiV1DomainsDnsrecordsUpdateSlaWindowDaysErrorComponent |
            ApiV1DomainsDnsrecordsUpdateSloAvailabilityErrorComponent | ApiV1DomainsDnsrecordsUpdateSloTargetErrorComponent
            | ApiV1DomainsDnsrecordsUpdateSloWindowDaysErrorComponent |
            ApiV1DomainsDnsrecordsUpdateTargetAvailabilityErrorComponent |
            ApiV1DomainsDnsrecordsUpdateTolerationsErrorComponent | ApiV1DomainsDnsrecordsUpdateTtlErrorComponent |
            ApiV1DomainsDnsrecordsUpdateTypeErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1DomainsDnsrecordsUpdateAnnotationsErrorComponent
        | ApiV1DomainsDnsrecordsUpdateArchivedAtErrorComponent
        | ApiV1DomainsDnsrecordsUpdateArchivedByErrorComponent
        | ApiV1DomainsDnsrecordsUpdateArchivedErrorComponent
        | ApiV1DomainsDnsrecordsUpdateArchivedReasonErrorComponent
        | ApiV1DomainsDnsrecordsUpdateContentErrorComponent
        | ApiV1DomainsDnsrecordsUpdateCreatedByComponentErrorComponent
        | ApiV1DomainsDnsrecordsUpdateCreatedByUserErrorComponent
        | ApiV1DomainsDnsrecordsUpdateCriticalityErrorComponent
        | ApiV1DomainsDnsrecordsUpdateDebugModeErrorComponent
        | ApiV1DomainsDnsrecordsUpdateDisplayNameErrorComponent
        | ApiV1DomainsDnsrecordsUpdateDnsZoneIdErrorComponent
        | ApiV1DomainsDnsrecordsUpdateKindErrorComponent
        | ApiV1DomainsDnsrecordsUpdateLabelsErrorComponent
        | ApiV1DomainsDnsrecordsUpdateLastReconciliationDurationSecondsErrorComponent
        | ApiV1DomainsDnsrecordsUpdateManagedByContentTypeErrorComponent
        | ApiV1DomainsDnsrecordsUpdateManagedByObjectIdErrorComponent
        | ApiV1DomainsDnsrecordsUpdateModifiedByUserErrorComponent
        | ApiV1DomainsDnsrecordsUpdateNameErrorComponent
        | ApiV1DomainsDnsrecordsUpdateNonFieldErrorsErrorComponent
        | ApiV1DomainsDnsrecordsUpdatePlatformDnsRecordCreatedErrorComponent
        | ApiV1DomainsDnsrecordsUpdatePlatformServiceErrorComponent
        | ApiV1DomainsDnsrecordsUpdatePriorityErrorComponent
        | ApiV1DomainsDnsrecordsUpdateProviderErrorComponent
        | ApiV1DomainsDnsrecordsUpdateProviderIdErrorComponent
        | ApiV1DomainsDnsrecordsUpdateProviderReferenceErrorComponent
        | ApiV1DomainsDnsrecordsUpdateReconciliationEnabledErrorComponent
        | ApiV1DomainsDnsrecordsUpdateSlaAvailabilityErrorComponent
        | ApiV1DomainsDnsrecordsUpdateSlaTargetErrorComponent
        | ApiV1DomainsDnsrecordsUpdateSlaWindowDaysErrorComponent
        | ApiV1DomainsDnsrecordsUpdateSloAvailabilityErrorComponent
        | ApiV1DomainsDnsrecordsUpdateSloTargetErrorComponent
        | ApiV1DomainsDnsrecordsUpdateSloWindowDaysErrorComponent
        | ApiV1DomainsDnsrecordsUpdateTargetAvailabilityErrorComponent
        | ApiV1DomainsDnsrecordsUpdateTolerationsErrorComponent
        | ApiV1DomainsDnsrecordsUpdateTtlErrorComponent
        | ApiV1DomainsDnsrecordsUpdateTypeErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_domains_dnsrecords_update_annotations_error_component import (
            ApiV1DomainsDnsrecordsUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_archived_at_error_component import (
            ApiV1DomainsDnsrecordsUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_archived_by_error_component import (
            ApiV1DomainsDnsrecordsUpdateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_archived_error_component import (
            ApiV1DomainsDnsrecordsUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_archived_reason_error_component import (
            ApiV1DomainsDnsrecordsUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_content_error_component import (
            ApiV1DomainsDnsrecordsUpdateContentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_created_by_component_error_component import (
            ApiV1DomainsDnsrecordsUpdateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_criticality_error_component import (
            ApiV1DomainsDnsrecordsUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_debug_mode_error_component import (
            ApiV1DomainsDnsrecordsUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_display_name_error_component import (
            ApiV1DomainsDnsrecordsUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_dns_zone_id_error_component import (
            ApiV1DomainsDnsrecordsUpdateDnsZoneIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_kind_error_component import (
            ApiV1DomainsDnsrecordsUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_labels_error_component import (
            ApiV1DomainsDnsrecordsUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_last_reconciliation_duration_seconds_error_component import (
            ApiV1DomainsDnsrecordsUpdateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_managed_by_content_type_error_component import (
            ApiV1DomainsDnsrecordsUpdateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_managed_by_object_id_error_component import (
            ApiV1DomainsDnsrecordsUpdateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_modified_by_user_error_component import (
            ApiV1DomainsDnsrecordsUpdateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_name_error_component import (
            ApiV1DomainsDnsrecordsUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_non_field_errors_error_component import (
            ApiV1DomainsDnsrecordsUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_platform_dns_record_created_error_component import (
            ApiV1DomainsDnsrecordsUpdatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_platform_service_error_component import (
            ApiV1DomainsDnsrecordsUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_priority_error_component import (
            ApiV1DomainsDnsrecordsUpdatePriorityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_provider_error_component import (
            ApiV1DomainsDnsrecordsUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_provider_id_error_component import (
            ApiV1DomainsDnsrecordsUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_provider_reference_error_component import (
            ApiV1DomainsDnsrecordsUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_reconciliation_enabled_error_component import (
            ApiV1DomainsDnsrecordsUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_sla_availability_error_component import (
            ApiV1DomainsDnsrecordsUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_sla_target_error_component import (
            ApiV1DomainsDnsrecordsUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_sla_window_days_error_component import (
            ApiV1DomainsDnsrecordsUpdateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_slo_availability_error_component import (
            ApiV1DomainsDnsrecordsUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_slo_target_error_component import (
            ApiV1DomainsDnsrecordsUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_slo_window_days_error_component import (
            ApiV1DomainsDnsrecordsUpdateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_target_availability_error_component import (
            ApiV1DomainsDnsrecordsUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_tolerations_error_component import (
            ApiV1DomainsDnsrecordsUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_ttl_error_component import (
            ApiV1DomainsDnsrecordsUpdateTtlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_type_error_component import (
            ApiV1DomainsDnsrecordsUpdateTypeErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1DomainsDnsrecordsUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsUpdateDnsZoneIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1DomainsDnsrecordsUpdateLastReconciliationDurationSecondsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsUpdateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsUpdateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsUpdateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsUpdateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsUpdatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsUpdateTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsUpdateContentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsUpdateTtlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsUpdatePriorityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsUpdateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsUpdateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsUpdateModifiedByUserErrorComponent):
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
        from ..models.api_v1_domains_dnsrecords_update_annotations_error_component import (
            ApiV1DomainsDnsrecordsUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_archived_at_error_component import (
            ApiV1DomainsDnsrecordsUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_archived_by_error_component import (
            ApiV1DomainsDnsrecordsUpdateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_archived_error_component import (
            ApiV1DomainsDnsrecordsUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_archived_reason_error_component import (
            ApiV1DomainsDnsrecordsUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_content_error_component import (
            ApiV1DomainsDnsrecordsUpdateContentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_created_by_component_error_component import (
            ApiV1DomainsDnsrecordsUpdateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_created_by_user_error_component import (
            ApiV1DomainsDnsrecordsUpdateCreatedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_criticality_error_component import (
            ApiV1DomainsDnsrecordsUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_debug_mode_error_component import (
            ApiV1DomainsDnsrecordsUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_display_name_error_component import (
            ApiV1DomainsDnsrecordsUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_dns_zone_id_error_component import (
            ApiV1DomainsDnsrecordsUpdateDnsZoneIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_kind_error_component import (
            ApiV1DomainsDnsrecordsUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_labels_error_component import (
            ApiV1DomainsDnsrecordsUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_last_reconciliation_duration_seconds_error_component import (
            ApiV1DomainsDnsrecordsUpdateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_managed_by_content_type_error_component import (
            ApiV1DomainsDnsrecordsUpdateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_managed_by_object_id_error_component import (
            ApiV1DomainsDnsrecordsUpdateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_modified_by_user_error_component import (
            ApiV1DomainsDnsrecordsUpdateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_name_error_component import (
            ApiV1DomainsDnsrecordsUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_non_field_errors_error_component import (
            ApiV1DomainsDnsrecordsUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_platform_dns_record_created_error_component import (
            ApiV1DomainsDnsrecordsUpdatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_platform_service_error_component import (
            ApiV1DomainsDnsrecordsUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_priority_error_component import (
            ApiV1DomainsDnsrecordsUpdatePriorityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_provider_error_component import (
            ApiV1DomainsDnsrecordsUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_provider_id_error_component import (
            ApiV1DomainsDnsrecordsUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_provider_reference_error_component import (
            ApiV1DomainsDnsrecordsUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_reconciliation_enabled_error_component import (
            ApiV1DomainsDnsrecordsUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_sla_availability_error_component import (
            ApiV1DomainsDnsrecordsUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_sla_target_error_component import (
            ApiV1DomainsDnsrecordsUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_sla_window_days_error_component import (
            ApiV1DomainsDnsrecordsUpdateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_slo_availability_error_component import (
            ApiV1DomainsDnsrecordsUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_slo_target_error_component import (
            ApiV1DomainsDnsrecordsUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_slo_window_days_error_component import (
            ApiV1DomainsDnsrecordsUpdateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_target_availability_error_component import (
            ApiV1DomainsDnsrecordsUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_tolerations_error_component import (
            ApiV1DomainsDnsrecordsUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_ttl_error_component import (
            ApiV1DomainsDnsrecordsUpdateTtlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnsrecords_update_type_error_component import (
            ApiV1DomainsDnsrecordsUpdateTypeErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1DomainsDnsrecordsUpdateAnnotationsErrorComponent
                | ApiV1DomainsDnsrecordsUpdateArchivedAtErrorComponent
                | ApiV1DomainsDnsrecordsUpdateArchivedByErrorComponent
                | ApiV1DomainsDnsrecordsUpdateArchivedErrorComponent
                | ApiV1DomainsDnsrecordsUpdateArchivedReasonErrorComponent
                | ApiV1DomainsDnsrecordsUpdateContentErrorComponent
                | ApiV1DomainsDnsrecordsUpdateCreatedByComponentErrorComponent
                | ApiV1DomainsDnsrecordsUpdateCreatedByUserErrorComponent
                | ApiV1DomainsDnsrecordsUpdateCriticalityErrorComponent
                | ApiV1DomainsDnsrecordsUpdateDebugModeErrorComponent
                | ApiV1DomainsDnsrecordsUpdateDisplayNameErrorComponent
                | ApiV1DomainsDnsrecordsUpdateDnsZoneIdErrorComponent
                | ApiV1DomainsDnsrecordsUpdateKindErrorComponent
                | ApiV1DomainsDnsrecordsUpdateLabelsErrorComponent
                | ApiV1DomainsDnsrecordsUpdateLastReconciliationDurationSecondsErrorComponent
                | ApiV1DomainsDnsrecordsUpdateManagedByContentTypeErrorComponent
                | ApiV1DomainsDnsrecordsUpdateManagedByObjectIdErrorComponent
                | ApiV1DomainsDnsrecordsUpdateModifiedByUserErrorComponent
                | ApiV1DomainsDnsrecordsUpdateNameErrorComponent
                | ApiV1DomainsDnsrecordsUpdateNonFieldErrorsErrorComponent
                | ApiV1DomainsDnsrecordsUpdatePlatformDnsRecordCreatedErrorComponent
                | ApiV1DomainsDnsrecordsUpdatePlatformServiceErrorComponent
                | ApiV1DomainsDnsrecordsUpdatePriorityErrorComponent
                | ApiV1DomainsDnsrecordsUpdateProviderErrorComponent
                | ApiV1DomainsDnsrecordsUpdateProviderIdErrorComponent
                | ApiV1DomainsDnsrecordsUpdateProviderReferenceErrorComponent
                | ApiV1DomainsDnsrecordsUpdateReconciliationEnabledErrorComponent
                | ApiV1DomainsDnsrecordsUpdateSlaAvailabilityErrorComponent
                | ApiV1DomainsDnsrecordsUpdateSlaTargetErrorComponent
                | ApiV1DomainsDnsrecordsUpdateSlaWindowDaysErrorComponent
                | ApiV1DomainsDnsrecordsUpdateSloAvailabilityErrorComponent
                | ApiV1DomainsDnsrecordsUpdateSloTargetErrorComponent
                | ApiV1DomainsDnsrecordsUpdateSloWindowDaysErrorComponent
                | ApiV1DomainsDnsrecordsUpdateTargetAvailabilityErrorComponent
                | ApiV1DomainsDnsrecordsUpdateTolerationsErrorComponent
                | ApiV1DomainsDnsrecordsUpdateTtlErrorComponent
                | ApiV1DomainsDnsrecordsUpdateTypeErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_update_error_type_0 = (
                        ApiV1DomainsDnsrecordsUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_update_error_type_1 = (
                        ApiV1DomainsDnsrecordsUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_update_error_type_2 = (
                        ApiV1DomainsDnsrecordsUpdateDnsZoneIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_update_error_type_3 = (
                        ApiV1DomainsDnsrecordsUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_update_error_type_4 = (
                        ApiV1DomainsDnsrecordsUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_update_error_type_5 = (
                        ApiV1DomainsDnsrecordsUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_update_error_type_6 = (
                        ApiV1DomainsDnsrecordsUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_update_error_type_7 = (
                        ApiV1DomainsDnsrecordsUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_update_error_type_8 = (
                        ApiV1DomainsDnsrecordsUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_update_error_type_9 = (
                        ApiV1DomainsDnsrecordsUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_update_error_type_10 = (
                        ApiV1DomainsDnsrecordsUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_update_error_type_11 = (
                        ApiV1DomainsDnsrecordsUpdateLastReconciliationDurationSecondsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_update_error_type_12 = (
                        ApiV1DomainsDnsrecordsUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_update_error_type_13 = (
                        ApiV1DomainsDnsrecordsUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_update_error_type_14 = (
                        ApiV1DomainsDnsrecordsUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_update_error_type_15 = (
                        ApiV1DomainsDnsrecordsUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_update_error_type_16 = (
                        ApiV1DomainsDnsrecordsUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_update_error_type_17 = (
                        ApiV1DomainsDnsrecordsUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_update_error_type_18 = (
                        ApiV1DomainsDnsrecordsUpdateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_update_error_type_19 = (
                        ApiV1DomainsDnsrecordsUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_update_error_type_20 = (
                        ApiV1DomainsDnsrecordsUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_update_error_type_21 = (
                        ApiV1DomainsDnsrecordsUpdateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_update_error_type_22 = (
                        ApiV1DomainsDnsrecordsUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_update_error_type_23 = (
                        ApiV1DomainsDnsrecordsUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_update_error_type_24 = (
                        ApiV1DomainsDnsrecordsUpdateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_update_error_type_25 = (
                        ApiV1DomainsDnsrecordsUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_update_error_type_26 = (
                        ApiV1DomainsDnsrecordsUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_update_error_type_27 = (
                        ApiV1DomainsDnsrecordsUpdateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_update_error_type_28 = (
                        ApiV1DomainsDnsrecordsUpdatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_update_error_type_29 = (
                        ApiV1DomainsDnsrecordsUpdateTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_update_error_type_30 = (
                        ApiV1DomainsDnsrecordsUpdateContentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_update_error_type_31 = (
                        ApiV1DomainsDnsrecordsUpdateTtlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_update_error_type_32 = (
                        ApiV1DomainsDnsrecordsUpdatePriorityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_update_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_update_error_type_33 = (
                        ApiV1DomainsDnsrecordsUpdateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_update_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_update_error_type_34 = (
                        ApiV1DomainsDnsrecordsUpdateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_update_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_update_error_type_35 = (
                        ApiV1DomainsDnsrecordsUpdateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_update_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_domains_dnsrecords_update_error_type_36 = (
                    ApiV1DomainsDnsrecordsUpdateCreatedByUserErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_domains_dnsrecords_update_error_type_36

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_domains_dnsrecords_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_domains_dnsrecords_update_validation_error.additional_properties = d
        return api_v1_domains_dnsrecords_update_validation_error

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
