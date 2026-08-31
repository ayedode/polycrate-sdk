from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_loadbalancers_regions_partial_update_active_error_component import (
        ApiV1LoadbalancersRegionsPartialUpdateActiveErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_partial_update_annotations_error_component import (
        ApiV1LoadbalancersRegionsPartialUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_partial_update_archived_at_error_component import (
        ApiV1LoadbalancersRegionsPartialUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_partial_update_archived_error_component import (
        ApiV1LoadbalancersRegionsPartialUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_partial_update_archived_reason_error_component import (
        ApiV1LoadbalancersRegionsPartialUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_partial_update_criticality_error_component import (
        ApiV1LoadbalancersRegionsPartialUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_partial_update_debug_mode_error_component import (
        ApiV1LoadbalancersRegionsPartialUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_partial_update_description_error_component import (
        ApiV1LoadbalancersRegionsPartialUpdateDescriptionErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_partial_update_display_name_error_component import (
        ApiV1LoadbalancersRegionsPartialUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_partial_update_external_traffic_policy_error_component import (
        ApiV1LoadbalancersRegionsPartialUpdateExternalTrafficPolicyErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_partial_update_kind_error_component import (
        ApiV1LoadbalancersRegionsPartialUpdateKindErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_partial_update_labels_error_component import (
        ApiV1LoadbalancersRegionsPartialUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_partial_update_name_error_component import (
        ApiV1LoadbalancersRegionsPartialUpdateNameErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_partial_update_non_field_errors_error_component import (
        ApiV1LoadbalancersRegionsPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_partial_update_platform_service_error_component import (
        ApiV1LoadbalancersRegionsPartialUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_partial_update_provider_error_component import (
        ApiV1LoadbalancersRegionsPartialUpdateProviderErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_partial_update_provider_id_error_component import (
        ApiV1LoadbalancersRegionsPartialUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_partial_update_provider_reference_error_component import (
        ApiV1LoadbalancersRegionsPartialUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_partial_update_reconciliation_enabled_error_component import (
        ApiV1LoadbalancersRegionsPartialUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_partial_update_region_config_error_component import (
        ApiV1LoadbalancersRegionsPartialUpdateRegionConfigErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_partial_update_region_name_error_component import (
        ApiV1LoadbalancersRegionsPartialUpdateRegionNameErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_partial_update_sla_availability_error_component import (
        ApiV1LoadbalancersRegionsPartialUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_partial_update_sla_target_error_component import (
        ApiV1LoadbalancersRegionsPartialUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_partial_update_slo_availability_error_component import (
        ApiV1LoadbalancersRegionsPartialUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_partial_update_slo_target_error_component import (
        ApiV1LoadbalancersRegionsPartialUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_partial_update_slug_error_component import (
        ApiV1LoadbalancersRegionsPartialUpdateSlugErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_partial_update_target_availability_error_component import (
        ApiV1LoadbalancersRegionsPartialUpdateTargetAvailabilityErrorComponent,
    )


T = TypeVar("T", bound="ApiV1LoadbalancersRegionsPartialUpdateValidationError")


@_attrs_define
class ApiV1LoadbalancersRegionsPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1LoadbalancersRegionsPartialUpdateActiveErrorComponent |
            ApiV1LoadbalancersRegionsPartialUpdateAnnotationsErrorComponent |
            ApiV1LoadbalancersRegionsPartialUpdateArchivedAtErrorComponent |
            ApiV1LoadbalancersRegionsPartialUpdateArchivedErrorComponent |
            ApiV1LoadbalancersRegionsPartialUpdateArchivedReasonErrorComponent |
            ApiV1LoadbalancersRegionsPartialUpdateCriticalityErrorComponent |
            ApiV1LoadbalancersRegionsPartialUpdateDebugModeErrorComponent |
            ApiV1LoadbalancersRegionsPartialUpdateDescriptionErrorComponent |
            ApiV1LoadbalancersRegionsPartialUpdateDisplayNameErrorComponent |
            ApiV1LoadbalancersRegionsPartialUpdateExternalTrafficPolicyErrorComponent |
            ApiV1LoadbalancersRegionsPartialUpdateKindErrorComponent |
            ApiV1LoadbalancersRegionsPartialUpdateLabelsErrorComponent |
            ApiV1LoadbalancersRegionsPartialUpdateNameErrorComponent |
            ApiV1LoadbalancersRegionsPartialUpdateNonFieldErrorsErrorComponent |
            ApiV1LoadbalancersRegionsPartialUpdatePlatformServiceErrorComponent |
            ApiV1LoadbalancersRegionsPartialUpdateProviderErrorComponent |
            ApiV1LoadbalancersRegionsPartialUpdateProviderIdErrorComponent |
            ApiV1LoadbalancersRegionsPartialUpdateProviderReferenceErrorComponent |
            ApiV1LoadbalancersRegionsPartialUpdateReconciliationEnabledErrorComponent |
            ApiV1LoadbalancersRegionsPartialUpdateRegionConfigErrorComponent |
            ApiV1LoadbalancersRegionsPartialUpdateRegionNameErrorComponent |
            ApiV1LoadbalancersRegionsPartialUpdateSlaAvailabilityErrorComponent |
            ApiV1LoadbalancersRegionsPartialUpdateSlaTargetErrorComponent |
            ApiV1LoadbalancersRegionsPartialUpdateSloAvailabilityErrorComponent |
            ApiV1LoadbalancersRegionsPartialUpdateSloTargetErrorComponent |
            ApiV1LoadbalancersRegionsPartialUpdateSlugErrorComponent |
            ApiV1LoadbalancersRegionsPartialUpdateTargetAvailabilityErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1LoadbalancersRegionsPartialUpdateActiveErrorComponent
        | ApiV1LoadbalancersRegionsPartialUpdateAnnotationsErrorComponent
        | ApiV1LoadbalancersRegionsPartialUpdateArchivedAtErrorComponent
        | ApiV1LoadbalancersRegionsPartialUpdateArchivedErrorComponent
        | ApiV1LoadbalancersRegionsPartialUpdateArchivedReasonErrorComponent
        | ApiV1LoadbalancersRegionsPartialUpdateCriticalityErrorComponent
        | ApiV1LoadbalancersRegionsPartialUpdateDebugModeErrorComponent
        | ApiV1LoadbalancersRegionsPartialUpdateDescriptionErrorComponent
        | ApiV1LoadbalancersRegionsPartialUpdateDisplayNameErrorComponent
        | ApiV1LoadbalancersRegionsPartialUpdateExternalTrafficPolicyErrorComponent
        | ApiV1LoadbalancersRegionsPartialUpdateKindErrorComponent
        | ApiV1LoadbalancersRegionsPartialUpdateLabelsErrorComponent
        | ApiV1LoadbalancersRegionsPartialUpdateNameErrorComponent
        | ApiV1LoadbalancersRegionsPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1LoadbalancersRegionsPartialUpdatePlatformServiceErrorComponent
        | ApiV1LoadbalancersRegionsPartialUpdateProviderErrorComponent
        | ApiV1LoadbalancersRegionsPartialUpdateProviderIdErrorComponent
        | ApiV1LoadbalancersRegionsPartialUpdateProviderReferenceErrorComponent
        | ApiV1LoadbalancersRegionsPartialUpdateReconciliationEnabledErrorComponent
        | ApiV1LoadbalancersRegionsPartialUpdateRegionConfigErrorComponent
        | ApiV1LoadbalancersRegionsPartialUpdateRegionNameErrorComponent
        | ApiV1LoadbalancersRegionsPartialUpdateSlaAvailabilityErrorComponent
        | ApiV1LoadbalancersRegionsPartialUpdateSlaTargetErrorComponent
        | ApiV1LoadbalancersRegionsPartialUpdateSloAvailabilityErrorComponent
        | ApiV1LoadbalancersRegionsPartialUpdateSloTargetErrorComponent
        | ApiV1LoadbalancersRegionsPartialUpdateSlugErrorComponent
        | ApiV1LoadbalancersRegionsPartialUpdateTargetAvailabilityErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_loadbalancers_regions_partial_update_active_error_component import (
            ApiV1LoadbalancersRegionsPartialUpdateActiveErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_partial_update_annotations_error_component import (
            ApiV1LoadbalancersRegionsPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_partial_update_archived_at_error_component import (
            ApiV1LoadbalancersRegionsPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_partial_update_archived_error_component import (
            ApiV1LoadbalancersRegionsPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_partial_update_archived_reason_error_component import (
            ApiV1LoadbalancersRegionsPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_partial_update_criticality_error_component import (
            ApiV1LoadbalancersRegionsPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_partial_update_debug_mode_error_component import (
            ApiV1LoadbalancersRegionsPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_partial_update_description_error_component import (
            ApiV1LoadbalancersRegionsPartialUpdateDescriptionErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_partial_update_display_name_error_component import (
            ApiV1LoadbalancersRegionsPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_partial_update_kind_error_component import (
            ApiV1LoadbalancersRegionsPartialUpdateKindErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_partial_update_labels_error_component import (
            ApiV1LoadbalancersRegionsPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_partial_update_name_error_component import (
            ApiV1LoadbalancersRegionsPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_partial_update_non_field_errors_error_component import (
            ApiV1LoadbalancersRegionsPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_partial_update_platform_service_error_component import (
            ApiV1LoadbalancersRegionsPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_partial_update_provider_error_component import (
            ApiV1LoadbalancersRegionsPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_partial_update_provider_id_error_component import (
            ApiV1LoadbalancersRegionsPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_partial_update_provider_reference_error_component import (
            ApiV1LoadbalancersRegionsPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_partial_update_reconciliation_enabled_error_component import (
            ApiV1LoadbalancersRegionsPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_partial_update_region_config_error_component import (
            ApiV1LoadbalancersRegionsPartialUpdateRegionConfigErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_partial_update_region_name_error_component import (
            ApiV1LoadbalancersRegionsPartialUpdateRegionNameErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_partial_update_sla_availability_error_component import (
            ApiV1LoadbalancersRegionsPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_partial_update_sla_target_error_component import (
            ApiV1LoadbalancersRegionsPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_partial_update_slo_availability_error_component import (
            ApiV1LoadbalancersRegionsPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_partial_update_slo_target_error_component import (
            ApiV1LoadbalancersRegionsPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_partial_update_slug_error_component import (
            ApiV1LoadbalancersRegionsPartialUpdateSlugErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_partial_update_target_availability_error_component import (
            ApiV1LoadbalancersRegionsPartialUpdateTargetAvailabilityErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1LoadbalancersRegionsPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsPartialUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsPartialUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsPartialUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsPartialUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsPartialUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsPartialUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsPartialUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1LoadbalancersRegionsPartialUpdateReconciliationEnabledErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsPartialUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsPartialUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsPartialUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsPartialUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsPartialUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsPartialUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsPartialUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsPartialUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsPartialUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsPartialUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsPartialUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsPartialUpdateSlugErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsPartialUpdateRegionNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsPartialUpdateActiveErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsPartialUpdateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsPartialUpdateRegionConfigErrorComponent):
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
        from ..models.api_v1_loadbalancers_regions_partial_update_active_error_component import (
            ApiV1LoadbalancersRegionsPartialUpdateActiveErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_partial_update_annotations_error_component import (
            ApiV1LoadbalancersRegionsPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_partial_update_archived_at_error_component import (
            ApiV1LoadbalancersRegionsPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_partial_update_archived_error_component import (
            ApiV1LoadbalancersRegionsPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_partial_update_archived_reason_error_component import (
            ApiV1LoadbalancersRegionsPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_partial_update_criticality_error_component import (
            ApiV1LoadbalancersRegionsPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_partial_update_debug_mode_error_component import (
            ApiV1LoadbalancersRegionsPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_partial_update_description_error_component import (
            ApiV1LoadbalancersRegionsPartialUpdateDescriptionErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_partial_update_display_name_error_component import (
            ApiV1LoadbalancersRegionsPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_partial_update_external_traffic_policy_error_component import (
            ApiV1LoadbalancersRegionsPartialUpdateExternalTrafficPolicyErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_partial_update_kind_error_component import (
            ApiV1LoadbalancersRegionsPartialUpdateKindErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_partial_update_labels_error_component import (
            ApiV1LoadbalancersRegionsPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_partial_update_name_error_component import (
            ApiV1LoadbalancersRegionsPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_partial_update_non_field_errors_error_component import (
            ApiV1LoadbalancersRegionsPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_partial_update_platform_service_error_component import (
            ApiV1LoadbalancersRegionsPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_partial_update_provider_error_component import (
            ApiV1LoadbalancersRegionsPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_partial_update_provider_id_error_component import (
            ApiV1LoadbalancersRegionsPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_partial_update_provider_reference_error_component import (
            ApiV1LoadbalancersRegionsPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_partial_update_reconciliation_enabled_error_component import (
            ApiV1LoadbalancersRegionsPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_partial_update_region_config_error_component import (
            ApiV1LoadbalancersRegionsPartialUpdateRegionConfigErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_partial_update_region_name_error_component import (
            ApiV1LoadbalancersRegionsPartialUpdateRegionNameErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_partial_update_sla_availability_error_component import (
            ApiV1LoadbalancersRegionsPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_partial_update_sla_target_error_component import (
            ApiV1LoadbalancersRegionsPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_partial_update_slo_availability_error_component import (
            ApiV1LoadbalancersRegionsPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_partial_update_slo_target_error_component import (
            ApiV1LoadbalancersRegionsPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_partial_update_slug_error_component import (
            ApiV1LoadbalancersRegionsPartialUpdateSlugErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_partial_update_target_availability_error_component import (
            ApiV1LoadbalancersRegionsPartialUpdateTargetAvailabilityErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1LoadbalancersRegionsPartialUpdateActiveErrorComponent
                | ApiV1LoadbalancersRegionsPartialUpdateAnnotationsErrorComponent
                | ApiV1LoadbalancersRegionsPartialUpdateArchivedAtErrorComponent
                | ApiV1LoadbalancersRegionsPartialUpdateArchivedErrorComponent
                | ApiV1LoadbalancersRegionsPartialUpdateArchivedReasonErrorComponent
                | ApiV1LoadbalancersRegionsPartialUpdateCriticalityErrorComponent
                | ApiV1LoadbalancersRegionsPartialUpdateDebugModeErrorComponent
                | ApiV1LoadbalancersRegionsPartialUpdateDescriptionErrorComponent
                | ApiV1LoadbalancersRegionsPartialUpdateDisplayNameErrorComponent
                | ApiV1LoadbalancersRegionsPartialUpdateExternalTrafficPolicyErrorComponent
                | ApiV1LoadbalancersRegionsPartialUpdateKindErrorComponent
                | ApiV1LoadbalancersRegionsPartialUpdateLabelsErrorComponent
                | ApiV1LoadbalancersRegionsPartialUpdateNameErrorComponent
                | ApiV1LoadbalancersRegionsPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1LoadbalancersRegionsPartialUpdatePlatformServiceErrorComponent
                | ApiV1LoadbalancersRegionsPartialUpdateProviderErrorComponent
                | ApiV1LoadbalancersRegionsPartialUpdateProviderIdErrorComponent
                | ApiV1LoadbalancersRegionsPartialUpdateProviderReferenceErrorComponent
                | ApiV1LoadbalancersRegionsPartialUpdateReconciliationEnabledErrorComponent
                | ApiV1LoadbalancersRegionsPartialUpdateRegionConfigErrorComponent
                | ApiV1LoadbalancersRegionsPartialUpdateRegionNameErrorComponent
                | ApiV1LoadbalancersRegionsPartialUpdateSlaAvailabilityErrorComponent
                | ApiV1LoadbalancersRegionsPartialUpdateSlaTargetErrorComponent
                | ApiV1LoadbalancersRegionsPartialUpdateSloAvailabilityErrorComponent
                | ApiV1LoadbalancersRegionsPartialUpdateSloTargetErrorComponent
                | ApiV1LoadbalancersRegionsPartialUpdateSlugErrorComponent
                | ApiV1LoadbalancersRegionsPartialUpdateTargetAvailabilityErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_partial_update_error_type_0 = (
                        ApiV1LoadbalancersRegionsPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_partial_update_error_type_1 = (
                        ApiV1LoadbalancersRegionsPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_partial_update_error_type_2 = (
                        ApiV1LoadbalancersRegionsPartialUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_partial_update_error_type_3 = (
                        ApiV1LoadbalancersRegionsPartialUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_partial_update_error_type_4 = (
                        ApiV1LoadbalancersRegionsPartialUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_partial_update_error_type_5 = (
                        ApiV1LoadbalancersRegionsPartialUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_partial_update_error_type_6 = (
                        ApiV1LoadbalancersRegionsPartialUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_partial_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_partial_update_error_type_7 = (
                        ApiV1LoadbalancersRegionsPartialUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_partial_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_partial_update_error_type_8 = (
                        ApiV1LoadbalancersRegionsPartialUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_partial_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_partial_update_error_type_9 = (
                        ApiV1LoadbalancersRegionsPartialUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_partial_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_partial_update_error_type_10 = (
                        ApiV1LoadbalancersRegionsPartialUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_partial_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_partial_update_error_type_11 = (
                        ApiV1LoadbalancersRegionsPartialUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_partial_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_partial_update_error_type_12 = (
                        ApiV1LoadbalancersRegionsPartialUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_partial_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_partial_update_error_type_13 = (
                        ApiV1LoadbalancersRegionsPartialUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_partial_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_partial_update_error_type_14 = (
                        ApiV1LoadbalancersRegionsPartialUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_partial_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_partial_update_error_type_15 = (
                        ApiV1LoadbalancersRegionsPartialUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_partial_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_partial_update_error_type_16 = (
                        ApiV1LoadbalancersRegionsPartialUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_partial_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_partial_update_error_type_17 = (
                        ApiV1LoadbalancersRegionsPartialUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_partial_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_partial_update_error_type_18 = (
                        ApiV1LoadbalancersRegionsPartialUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_partial_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_partial_update_error_type_19 = (
                        ApiV1LoadbalancersRegionsPartialUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_partial_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_partial_update_error_type_20 = (
                        ApiV1LoadbalancersRegionsPartialUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_partial_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_partial_update_error_type_21 = (
                        ApiV1LoadbalancersRegionsPartialUpdateSlugErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_partial_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_partial_update_error_type_22 = (
                        ApiV1LoadbalancersRegionsPartialUpdateRegionNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_partial_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_partial_update_error_type_23 = (
                        ApiV1LoadbalancersRegionsPartialUpdateActiveErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_partial_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_partial_update_error_type_24 = (
                        ApiV1LoadbalancersRegionsPartialUpdateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_partial_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_partial_update_error_type_25 = (
                        ApiV1LoadbalancersRegionsPartialUpdateRegionConfigErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_partial_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_loadbalancers_regions_partial_update_error_type_26 = (
                    ApiV1LoadbalancersRegionsPartialUpdateExternalTrafficPolicyErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_loadbalancers_regions_partial_update_error_type_26

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_loadbalancers_regions_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_loadbalancers_regions_partial_update_validation_error.additional_properties = d
        return api_v1_loadbalancers_regions_partial_update_validation_error

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
