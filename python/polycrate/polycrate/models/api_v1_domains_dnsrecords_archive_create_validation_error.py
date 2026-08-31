from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_domains_dnsrecords_archive_create_annotations_error_component import (
        ApiV1DomainsDnsrecordsArchiveCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_archive_create_archived_at_error_component import (
        ApiV1DomainsDnsrecordsArchiveCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_archive_create_archived_by_error_component import (
        ApiV1DomainsDnsrecordsArchiveCreateArchivedByErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_archive_create_archived_error_component import (
        ApiV1DomainsDnsrecordsArchiveCreateArchivedErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_archive_create_archived_reason_error_component import (
        ApiV1DomainsDnsrecordsArchiveCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_archive_create_content_error_component import (
        ApiV1DomainsDnsrecordsArchiveCreateContentErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_archive_create_created_by_component_error_component import (
        ApiV1DomainsDnsrecordsArchiveCreateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_archive_create_created_by_user_error_component import (
        ApiV1DomainsDnsrecordsArchiveCreateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_archive_create_criticality_error_component import (
        ApiV1DomainsDnsrecordsArchiveCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_archive_create_debug_mode_error_component import (
        ApiV1DomainsDnsrecordsArchiveCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_archive_create_display_name_error_component import (
        ApiV1DomainsDnsrecordsArchiveCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_archive_create_dns_zone_id_error_component import (
        ApiV1DomainsDnsrecordsArchiveCreateDnsZoneIdErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_archive_create_kind_error_component import (
        ApiV1DomainsDnsrecordsArchiveCreateKindErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_archive_create_labels_error_component import (
        ApiV1DomainsDnsrecordsArchiveCreateLabelsErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_archive_create_last_reconciliation_duration_seconds_error_component import (
        ApiV1DomainsDnsrecordsArchiveCreateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_archive_create_managed_by_content_type_error_component import (
        ApiV1DomainsDnsrecordsArchiveCreateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_archive_create_managed_by_object_id_error_component import (
        ApiV1DomainsDnsrecordsArchiveCreateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_archive_create_modified_by_user_error_component import (
        ApiV1DomainsDnsrecordsArchiveCreateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_archive_create_name_error_component import (
        ApiV1DomainsDnsrecordsArchiveCreateNameErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_archive_create_non_field_errors_error_component import (
        ApiV1DomainsDnsrecordsArchiveCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_archive_create_platform_dns_record_created_error_component import (
        ApiV1DomainsDnsrecordsArchiveCreatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_archive_create_platform_service_error_component import (
        ApiV1DomainsDnsrecordsArchiveCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_archive_create_priority_error_component import (
        ApiV1DomainsDnsrecordsArchiveCreatePriorityErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_archive_create_provider_error_component import (
        ApiV1DomainsDnsrecordsArchiveCreateProviderErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_archive_create_provider_id_error_component import (
        ApiV1DomainsDnsrecordsArchiveCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_archive_create_provider_reference_error_component import (
        ApiV1DomainsDnsrecordsArchiveCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_archive_create_reconciliation_enabled_error_component import (
        ApiV1DomainsDnsrecordsArchiveCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_archive_create_sla_availability_error_component import (
        ApiV1DomainsDnsrecordsArchiveCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_archive_create_sla_target_error_component import (
        ApiV1DomainsDnsrecordsArchiveCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_archive_create_sla_window_days_error_component import (
        ApiV1DomainsDnsrecordsArchiveCreateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_archive_create_slo_availability_error_component import (
        ApiV1DomainsDnsrecordsArchiveCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_archive_create_slo_target_error_component import (
        ApiV1DomainsDnsrecordsArchiveCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_archive_create_slo_window_days_error_component import (
        ApiV1DomainsDnsrecordsArchiveCreateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_archive_create_target_availability_error_component import (
        ApiV1DomainsDnsrecordsArchiveCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_archive_create_tolerations_error_component import (
        ApiV1DomainsDnsrecordsArchiveCreateTolerationsErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_archive_create_ttl_error_component import (
        ApiV1DomainsDnsrecordsArchiveCreateTtlErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_archive_create_type_error_component import (
        ApiV1DomainsDnsrecordsArchiveCreateTypeErrorComponent,
    )


T = TypeVar("T", bound="ApiV1DomainsDnsrecordsArchiveCreateValidationError")


@_attrs_define
class ApiV1DomainsDnsrecordsArchiveCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1DomainsDnsrecordsArchiveCreateAnnotationsErrorComponent |
            ApiV1DomainsDnsrecordsArchiveCreateArchivedAtErrorComponent |
            ApiV1DomainsDnsrecordsArchiveCreateArchivedByErrorComponent |
            ApiV1DomainsDnsrecordsArchiveCreateArchivedErrorComponent |
            ApiV1DomainsDnsrecordsArchiveCreateArchivedReasonErrorComponent |
            ApiV1DomainsDnsrecordsArchiveCreateContentErrorComponent |
            ApiV1DomainsDnsrecordsArchiveCreateCreatedByComponentErrorComponent |
            ApiV1DomainsDnsrecordsArchiveCreateCreatedByUserErrorComponent |
            ApiV1DomainsDnsrecordsArchiveCreateCriticalityErrorComponent |
            ApiV1DomainsDnsrecordsArchiveCreateDebugModeErrorComponent |
            ApiV1DomainsDnsrecordsArchiveCreateDisplayNameErrorComponent |
            ApiV1DomainsDnsrecordsArchiveCreateDnsZoneIdErrorComponent |
            ApiV1DomainsDnsrecordsArchiveCreateKindErrorComponent | ApiV1DomainsDnsrecordsArchiveCreateLabelsErrorComponent
            | ApiV1DomainsDnsrecordsArchiveCreateLastReconciliationDurationSecondsErrorComponent |
            ApiV1DomainsDnsrecordsArchiveCreateManagedByContentTypeErrorComponent |
            ApiV1DomainsDnsrecordsArchiveCreateManagedByObjectIdErrorComponent |
            ApiV1DomainsDnsrecordsArchiveCreateModifiedByUserErrorComponent |
            ApiV1DomainsDnsrecordsArchiveCreateNameErrorComponent |
            ApiV1DomainsDnsrecordsArchiveCreateNonFieldErrorsErrorComponent |
            ApiV1DomainsDnsrecordsArchiveCreatePlatformDnsRecordCreatedErrorComponent |
            ApiV1DomainsDnsrecordsArchiveCreatePlatformServiceErrorComponent |
            ApiV1DomainsDnsrecordsArchiveCreatePriorityErrorComponent |
            ApiV1DomainsDnsrecordsArchiveCreateProviderErrorComponent |
            ApiV1DomainsDnsrecordsArchiveCreateProviderIdErrorComponent |
            ApiV1DomainsDnsrecordsArchiveCreateProviderReferenceErrorComponent |
            ApiV1DomainsDnsrecordsArchiveCreateReconciliationEnabledErrorComponent |
            ApiV1DomainsDnsrecordsArchiveCreateSlaAvailabilityErrorComponent |
            ApiV1DomainsDnsrecordsArchiveCreateSlaTargetErrorComponent |
            ApiV1DomainsDnsrecordsArchiveCreateSlaWindowDaysErrorComponent |
            ApiV1DomainsDnsrecordsArchiveCreateSloAvailabilityErrorComponent |
            ApiV1DomainsDnsrecordsArchiveCreateSloTargetErrorComponent |
            ApiV1DomainsDnsrecordsArchiveCreateSloWindowDaysErrorComponent |
            ApiV1DomainsDnsrecordsArchiveCreateTargetAvailabilityErrorComponent |
            ApiV1DomainsDnsrecordsArchiveCreateTolerationsErrorComponent |
            ApiV1DomainsDnsrecordsArchiveCreateTtlErrorComponent | ApiV1DomainsDnsrecordsArchiveCreateTypeErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1DomainsDnsrecordsArchiveCreateAnnotationsErrorComponent
        | ApiV1DomainsDnsrecordsArchiveCreateArchivedAtErrorComponent
        | ApiV1DomainsDnsrecordsArchiveCreateArchivedByErrorComponent
        | ApiV1DomainsDnsrecordsArchiveCreateArchivedErrorComponent
        | ApiV1DomainsDnsrecordsArchiveCreateArchivedReasonErrorComponent
        | ApiV1DomainsDnsrecordsArchiveCreateContentErrorComponent
        | ApiV1DomainsDnsrecordsArchiveCreateCreatedByComponentErrorComponent
        | ApiV1DomainsDnsrecordsArchiveCreateCreatedByUserErrorComponent
        | ApiV1DomainsDnsrecordsArchiveCreateCriticalityErrorComponent
        | ApiV1DomainsDnsrecordsArchiveCreateDebugModeErrorComponent
        | ApiV1DomainsDnsrecordsArchiveCreateDisplayNameErrorComponent
        | ApiV1DomainsDnsrecordsArchiveCreateDnsZoneIdErrorComponent
        | ApiV1DomainsDnsrecordsArchiveCreateKindErrorComponent
        | ApiV1DomainsDnsrecordsArchiveCreateLabelsErrorComponent
        | ApiV1DomainsDnsrecordsArchiveCreateLastReconciliationDurationSecondsErrorComponent
        | ApiV1DomainsDnsrecordsArchiveCreateManagedByContentTypeErrorComponent
        | ApiV1DomainsDnsrecordsArchiveCreateManagedByObjectIdErrorComponent
        | ApiV1DomainsDnsrecordsArchiveCreateModifiedByUserErrorComponent
        | ApiV1DomainsDnsrecordsArchiveCreateNameErrorComponent
        | ApiV1DomainsDnsrecordsArchiveCreateNonFieldErrorsErrorComponent
        | ApiV1DomainsDnsrecordsArchiveCreatePlatformDnsRecordCreatedErrorComponent
        | ApiV1DomainsDnsrecordsArchiveCreatePlatformServiceErrorComponent
        | ApiV1DomainsDnsrecordsArchiveCreatePriorityErrorComponent
        | ApiV1DomainsDnsrecordsArchiveCreateProviderErrorComponent
        | ApiV1DomainsDnsrecordsArchiveCreateProviderIdErrorComponent
        | ApiV1DomainsDnsrecordsArchiveCreateProviderReferenceErrorComponent
        | ApiV1DomainsDnsrecordsArchiveCreateReconciliationEnabledErrorComponent
        | ApiV1DomainsDnsrecordsArchiveCreateSlaAvailabilityErrorComponent
        | ApiV1DomainsDnsrecordsArchiveCreateSlaTargetErrorComponent
        | ApiV1DomainsDnsrecordsArchiveCreateSlaWindowDaysErrorComponent
        | ApiV1DomainsDnsrecordsArchiveCreateSloAvailabilityErrorComponent
        | ApiV1DomainsDnsrecordsArchiveCreateSloTargetErrorComponent
        | ApiV1DomainsDnsrecordsArchiveCreateSloWindowDaysErrorComponent
        | ApiV1DomainsDnsrecordsArchiveCreateTargetAvailabilityErrorComponent
        | ApiV1DomainsDnsrecordsArchiveCreateTolerationsErrorComponent
        | ApiV1DomainsDnsrecordsArchiveCreateTtlErrorComponent
        | ApiV1DomainsDnsrecordsArchiveCreateTypeErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_domains_dnsrecords_archive_create_annotations_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_archived_at_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_archived_by_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreateArchivedByErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_archived_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreateArchivedErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_archived_reason_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_content_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreateContentErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_created_by_component_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_criticality_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_debug_mode_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_display_name_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_dns_zone_id_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreateDnsZoneIdErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_kind_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreateKindErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_labels_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreateLabelsErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_managed_by_content_type_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_managed_by_object_id_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_modified_by_user_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreateModifiedByUserErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_name_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreateNameErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_non_field_errors_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_platform_dns_record_created_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_platform_service_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_priority_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreatePriorityErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_provider_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreateProviderErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_provider_id_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_provider_reference_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_reconciliation_enabled_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_sla_availability_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_sla_target_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_sla_window_days_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_slo_availability_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_slo_target_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_slo_window_days_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_target_availability_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_tolerations_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreateTolerationsErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_ttl_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreateTtlErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_type_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreateTypeErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1DomainsDnsrecordsArchiveCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsArchiveCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsArchiveCreateDnsZoneIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsArchiveCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsArchiveCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsArchiveCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsArchiveCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsArchiveCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsArchiveCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsArchiveCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsArchiveCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1DomainsDnsrecordsArchiveCreateLastReconciliationDurationSecondsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsArchiveCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsArchiveCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsArchiveCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsArchiveCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsArchiveCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsArchiveCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsArchiveCreateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsArchiveCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsArchiveCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsArchiveCreateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsArchiveCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsArchiveCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsArchiveCreateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsArchiveCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsArchiveCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsArchiveCreateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1DomainsDnsrecordsArchiveCreatePlatformDnsRecordCreatedErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsArchiveCreateTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsArchiveCreateContentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsArchiveCreateTtlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsArchiveCreatePriorityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsArchiveCreateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsArchiveCreateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsArchiveCreateModifiedByUserErrorComponent):
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
        from ..models.api_v1_domains_dnsrecords_archive_create_annotations_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_archived_at_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_archived_by_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreateArchivedByErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_archived_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreateArchivedErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_archived_reason_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_content_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreateContentErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_created_by_component_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_created_by_user_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreateCreatedByUserErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_criticality_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_debug_mode_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_display_name_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_dns_zone_id_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreateDnsZoneIdErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_kind_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreateKindErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_labels_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreateLabelsErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_managed_by_content_type_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_managed_by_object_id_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_modified_by_user_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreateModifiedByUserErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_name_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreateNameErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_non_field_errors_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_platform_dns_record_created_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_platform_service_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_priority_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreatePriorityErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_provider_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreateProviderErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_provider_id_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_provider_reference_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_reconciliation_enabled_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_sla_availability_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_sla_target_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_sla_window_days_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_slo_availability_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_slo_target_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_slo_window_days_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_target_availability_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_tolerations_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreateTolerationsErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_ttl_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreateTtlErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_archive_create_type_error_component import (
            ApiV1DomainsDnsrecordsArchiveCreateTypeErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1DomainsDnsrecordsArchiveCreateAnnotationsErrorComponent
                | ApiV1DomainsDnsrecordsArchiveCreateArchivedAtErrorComponent
                | ApiV1DomainsDnsrecordsArchiveCreateArchivedByErrorComponent
                | ApiV1DomainsDnsrecordsArchiveCreateArchivedErrorComponent
                | ApiV1DomainsDnsrecordsArchiveCreateArchivedReasonErrorComponent
                | ApiV1DomainsDnsrecordsArchiveCreateContentErrorComponent
                | ApiV1DomainsDnsrecordsArchiveCreateCreatedByComponentErrorComponent
                | ApiV1DomainsDnsrecordsArchiveCreateCreatedByUserErrorComponent
                | ApiV1DomainsDnsrecordsArchiveCreateCriticalityErrorComponent
                | ApiV1DomainsDnsrecordsArchiveCreateDebugModeErrorComponent
                | ApiV1DomainsDnsrecordsArchiveCreateDisplayNameErrorComponent
                | ApiV1DomainsDnsrecordsArchiveCreateDnsZoneIdErrorComponent
                | ApiV1DomainsDnsrecordsArchiveCreateKindErrorComponent
                | ApiV1DomainsDnsrecordsArchiveCreateLabelsErrorComponent
                | ApiV1DomainsDnsrecordsArchiveCreateLastReconciliationDurationSecondsErrorComponent
                | ApiV1DomainsDnsrecordsArchiveCreateManagedByContentTypeErrorComponent
                | ApiV1DomainsDnsrecordsArchiveCreateManagedByObjectIdErrorComponent
                | ApiV1DomainsDnsrecordsArchiveCreateModifiedByUserErrorComponent
                | ApiV1DomainsDnsrecordsArchiveCreateNameErrorComponent
                | ApiV1DomainsDnsrecordsArchiveCreateNonFieldErrorsErrorComponent
                | ApiV1DomainsDnsrecordsArchiveCreatePlatformDnsRecordCreatedErrorComponent
                | ApiV1DomainsDnsrecordsArchiveCreatePlatformServiceErrorComponent
                | ApiV1DomainsDnsrecordsArchiveCreatePriorityErrorComponent
                | ApiV1DomainsDnsrecordsArchiveCreateProviderErrorComponent
                | ApiV1DomainsDnsrecordsArchiveCreateProviderIdErrorComponent
                | ApiV1DomainsDnsrecordsArchiveCreateProviderReferenceErrorComponent
                | ApiV1DomainsDnsrecordsArchiveCreateReconciliationEnabledErrorComponent
                | ApiV1DomainsDnsrecordsArchiveCreateSlaAvailabilityErrorComponent
                | ApiV1DomainsDnsrecordsArchiveCreateSlaTargetErrorComponent
                | ApiV1DomainsDnsrecordsArchiveCreateSlaWindowDaysErrorComponent
                | ApiV1DomainsDnsrecordsArchiveCreateSloAvailabilityErrorComponent
                | ApiV1DomainsDnsrecordsArchiveCreateSloTargetErrorComponent
                | ApiV1DomainsDnsrecordsArchiveCreateSloWindowDaysErrorComponent
                | ApiV1DomainsDnsrecordsArchiveCreateTargetAvailabilityErrorComponent
                | ApiV1DomainsDnsrecordsArchiveCreateTolerationsErrorComponent
                | ApiV1DomainsDnsrecordsArchiveCreateTtlErrorComponent
                | ApiV1DomainsDnsrecordsArchiveCreateTypeErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_0 = (
                        ApiV1DomainsDnsrecordsArchiveCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_1 = (
                        ApiV1DomainsDnsrecordsArchiveCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_2 = (
                        ApiV1DomainsDnsrecordsArchiveCreateDnsZoneIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_3 = (
                        ApiV1DomainsDnsrecordsArchiveCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_4 = (
                        ApiV1DomainsDnsrecordsArchiveCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_5 = (
                        ApiV1DomainsDnsrecordsArchiveCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_6 = (
                        ApiV1DomainsDnsrecordsArchiveCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_7 = (
                        ApiV1DomainsDnsrecordsArchiveCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_8 = (
                        ApiV1DomainsDnsrecordsArchiveCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_9 = (
                        ApiV1DomainsDnsrecordsArchiveCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_10 = (
                        ApiV1DomainsDnsrecordsArchiveCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_11 = (
                        ApiV1DomainsDnsrecordsArchiveCreateLastReconciliationDurationSecondsErrorComponent.from_dict(
                            data
                        )
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_12 = (
                        ApiV1DomainsDnsrecordsArchiveCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_13 = (
                        ApiV1DomainsDnsrecordsArchiveCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_14 = (
                        ApiV1DomainsDnsrecordsArchiveCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_15 = (
                        ApiV1DomainsDnsrecordsArchiveCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_16 = (
                        ApiV1DomainsDnsrecordsArchiveCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_17 = (
                        ApiV1DomainsDnsrecordsArchiveCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_18 = (
                        ApiV1DomainsDnsrecordsArchiveCreateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_19 = (
                        ApiV1DomainsDnsrecordsArchiveCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_20 = (
                        ApiV1DomainsDnsrecordsArchiveCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_21 = (
                        ApiV1DomainsDnsrecordsArchiveCreateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_22 = (
                        ApiV1DomainsDnsrecordsArchiveCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_23 = (
                        ApiV1DomainsDnsrecordsArchiveCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_24 = (
                        ApiV1DomainsDnsrecordsArchiveCreateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_25 = (
                        ApiV1DomainsDnsrecordsArchiveCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_26 = (
                        ApiV1DomainsDnsrecordsArchiveCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_27 = (
                        ApiV1DomainsDnsrecordsArchiveCreateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_28 = (
                        ApiV1DomainsDnsrecordsArchiveCreatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_29 = (
                        ApiV1DomainsDnsrecordsArchiveCreateTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_30 = (
                        ApiV1DomainsDnsrecordsArchiveCreateContentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_31 = (
                        ApiV1DomainsDnsrecordsArchiveCreateTtlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_32 = (
                        ApiV1DomainsDnsrecordsArchiveCreatePriorityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_33 = (
                        ApiV1DomainsDnsrecordsArchiveCreateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_34 = (
                        ApiV1DomainsDnsrecordsArchiveCreateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_35 = (
                        ApiV1DomainsDnsrecordsArchiveCreateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_36 = (
                    ApiV1DomainsDnsrecordsArchiveCreateCreatedByUserErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_domains_dnsrecords_archive_create_error_type_36

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_domains_dnsrecords_archive_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_domains_dnsrecords_archive_create_validation_error.additional_properties = d
        return api_v1_domains_dnsrecords_archive_create_validation_error

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
